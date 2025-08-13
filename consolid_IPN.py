# -*- coding: utf-8 -*-
"""
Збір вхідних ПН/РК за травень 2025 з усіх Excel-файлів і аркушів.
Фільтр: 'ЄДРПОУ покупця' == 0
Колонки у виході:
  'ЄДРПОУ продавця', 'ІНН покупця', 'ЄДРПОУ покупця',
  'Дата виписки ПН/РК', 'Номер ПН/РК',
  'Номенклатура товару', 'Код товару згідно УКТЗЕД'
"""

import os
import sys
import glob
import pandas as pd

# --- ВХІДНІ ПАРАМЕТРИ ---
INPUT_DIR = r"F:\Олег\СЗР_входящие\2025-05\травень 2025 основні_1\╤В╤А╨░╨▓╨╡╨╜╤М 2025 ╨╛╤Б╨╜╨╛╨▓╨╜╤Ц_1"
OUTPUT_DIR = r"F:\Олег\СЗР_входящие\Зведені"
OUTPUT_NAME = "Вхід_2025-05_додатковіІПН.xlsx"  # додав розширення .xlsx

REQUIRED_COLS = [
    "ЄДРПОУ продавця",
    "ІНН покупця",
    "ЄДРПОУ покупця",
    "Дата виписки ПН/РК",
    "Номер ПН/РК",
    "Номенклатура товару",
    "Код товару згідно УКТЗЕД",
]

# --- НАЛАШТУВАННЯ ВИВОДУ ---
pd.options.display.max_columns = 0

def read_all_sheets(path: str):
    """
    Прочитати всі аркуші з Excel-файлу у вигляді словника {sheet_name: DataFrame}.
    Підтримка: .xlsx/.xlsm напряму; .xlsb - якщо встановлено pyxlsb; .xls пропускаємо.
    """
    ext = os.path.splitext(path)[1].lower()

    if ext in [".xlsx", ".xlsm"]:
        return pd.read_excel(path, sheet_name=None, dtype=object, engine="openpyxl")
    elif ext == ".xlsb":
        # Потрібен пакет pyxlsb
        try:
            return pd.read_excel(path, sheet_name=None, dtype=object, engine="pyxlsb")
        except Exception as e:
            print(f"[ПОПЕРЕДЖЕННЯ] Не вдалося прочитати .xlsb (потрібен pyxlsb): {path}\n  → {e}")
            return {}
    else:
        # .xls та інші — пропускаємо, щоб уникнути проблем з xlrd
        print(f"[ІНФО] Пропускаю файл з непідтримуваним розширенням: {path}")
        return {}

def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Уніфікуємо назви колонок: обрізаємо пробіли, приводимо до точного збігу
    (без зміни регістру, бо потрібні українські назви).
    Також прибираємо приховані \n/\r.
    """
    df = df.copy()
    df.columns = [str(c).replace("\n", " ").replace("\r", " ").strip() for c in df.columns]
    return df

def filter_edrpou_zero(df: pd.DataFrame) -> pd.DataFrame:
    """
    Фільтрація рядків, де 'ЄДРПОУ покупця' == 0.
    Враховує можливі типи (int/float/str) і пробіли.
    """
    col = "ЄДРПОУ покупця"
    if col not in df.columns:
        return df.iloc[0:0]  # пуста таблиця з такими ж колонками

    s = df[col]

    # маска 1: числовий нуль (0 або 0.0)
    mask_num_zero = s.eq(0)

    # маска 2: текстове "0" з можливими пробілами
    s_str = s.astype(str).str.strip()
    mask_str_zero = s_str.eq("0")

    mask = mask_num_zero | mask_str_zero
    return df[mask]

def keep_required_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Залишаємо лише потрібні колонки в заданому порядку.
    Якщо чогось бракує — додаємо порожні стовпці, щоб не злітав порядок.
    """
    df = df.copy()
    for c in REQUIRED_COLS:
        if c not in df.columns:
            df[c] = pd.NA
    return df[REQUIRED_COLS]

def main():
    if not os.path.isdir(INPUT_DIR):
        print(f"[ПОМИЛКА] Не знайдено вхідну папку: {INPUT_DIR}")
        sys.exit(1)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_NAME)

    patterns = [
        os.path.join(INPUT_DIR, "*.xlsx"),
        os.path.join(INPUT_DIR, "*.xlsm"),
        os.path.join(INPUT_DIR, "*.xlsb"),
        os.path.join(INPUT_DIR, "*.xls"),  # буде пропущено, але покажемо інформаційне повідомлення
    ]
    files = []
    for p in patterns:
        files.extend(glob.glob(p))

    if not files:
        print(f"[ІНФО] У папці нема Excel-файлів: {INPUT_DIR}")
        # все одно створимо порожній файл з заголовками
        empty_df = pd.DataFrame(columns=REQUIRED_COLS)
        empty_df.to_excel(output_path, index=False)
        print(f"[ГОТОВО] Створено порожній файл: {output_path}")
        return

    collected = []
    total_rows_before = 0
    total_rows_after = 0

    for f in files:
        try:
            sheets = read_all_sheets(f)
        except Exception as e:
            print(f"[ПОМИЛКА] Не вдалося прочитати файл: {f}\n  → {e}")
            continue

        if not sheets:
            continue

        for sh_name, df in sheets.items():
            if df is None or df.empty:
                continue

            try:
                df = normalize_columns(df)
                total_rows_before += len(df)
                df = filter_edrpou_zero(df)
                if df.empty:
                    continue
                df = keep_required_columns(df)
                df["_Файл"] = os.path.basename(f)
                df["_Лист"] = str(sh_name)
                collected.append(df)
                total_rows_after += len(df)
            except Exception as e:
                print(f"[ПОПЕРЕДЖЕННЯ] Проблема з обробкою: файл={f}, аркуш={sh_name}\n  → {e}")

    if collected:
        result = pd.concat(collected, ignore_index=True)
    else:
        result = pd.DataFrame(columns=REQUIRED_COLS + ["_Файл", "_Лист"])

    # Зберігаємо у .xlsx (openpyxl)
    try:
        # коректна дата збережеться як є, оскільки ми читали dtype=object.
        # Якщо вхід був датою Excel, вона мігрує як datetime або str — залишаємо як є.
        result.to_excel(output_path, index=False, engine="openpyxl")
    except Exception as e:
        print(f"[ПОМИЛКА] Не вдалося записати у файл {output_path}\n  → {e}")
        sys.exit(1)

    print(f"[ГОТОВО] Записано: {output_path}")
    print(f"  Файлів опрацьовано: {len(files)}")
    print(f"  Рядків вхідних (усіх аркушів): {total_rows_before}")
    print(f"  Рядків після фільтру ('ЄДРПОУ покупця' == 0): {total_rows_after}")
    print(f"  Форма підсумкової таблиці: {result.shape}")
    if result.empty:
        print("  [УВАГА] Порожній результат — або немає рядків із '0', або відсутня потрібна колонка у файлах.")
    else:
        # короткий прев'ю
        print(result.head(min(5, len(result))))

if __name__ == "__main__":
    main()
