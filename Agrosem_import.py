# -*- coding: utf-8 -*-
"""
Збирання Excel-файлів з папки, фільтрація за кодами з окремого файлу (колонка A),
видалення перших 2 рядків у кожному файлі, об'єднання та збереження результату.

Автор: Олегу
"""

import os
from pathlib import Path
import pandas as pd

# ===== НАЛАШТУВАННЯ ШЛЯХІВ =====
# Папка з вихідними файлами (саме ця, без підпапок; за потреби можна додати recursive)
SRC_DIR = Path(r"F:\Олег\Агросем\імпорт експорт 2025 Агросем квітень_липень 2025\╤Ц╨╝╨┐╨╛╤А╤В ╨╡╨║╤Б╨┐╨╛╤А╤В 2025 ╨Р╨│╤А╨╛╤Б╨╡╨╝ ╨▒╨╡╤А╨╡╨╖╨╡╨╜╤М_╨╗╨╕╨┐╨╡╨╜╤М 2025")

# Файл із переліком кодів (беремо колону A)
CODES_XLSX = Path(r"F:\Олег\Агросем\Перелік кодів для Агросем експорт_імпорт_квітень-липень 2025.xlsx")

# Вихідна папка та назва файлу
OUT_DIR = Path(r"F:\Олег\Агросем")
OUT_NAME = "Агросем_імпорт_04-07.2025.xlsx"   # записуємо у формат .xlsx

# ===== ПАРАМЕТРИ ОБРОБКИ =====
# Колонка для фільтрації "L" -> це 12-та колонка, індекс 11 (нульова індексація)
FILTER_COL_IDX = 11  # тобто "L"
# У кожному файлі перші 2 рядки потрібно видалити
SKIP_ROWS = 2

# Які розширення беремо (xls може вимагати xlrd; якщо його немає — пропустимо)
EXCEL_EXTS = {".xlsx", ".xls", ".xlsm", ".xlsb"}

# ===== КОРИСНІ ФУНКЦІЇ =====
def normalize_code_series(s: pd.Series) -> pd.Series:
    """Нормалізуємо коди для коректного порівняння: у str, trim, без NAN."""
    return (
        s.astype(str)
         .str.strip()
         .str.replace("\u00A0", " ", regex=False)  # non-breaking space -> space
    )

def read_codes_list(codes_path: Path) -> set:
    """Зчитуємо коди з колонки A (першої) файлу з кодами та повертаємо як множину (str)."""
    df_codes = pd.read_excel(codes_path, header=None, usecols=[0])
    codes = normalize_code_series(df_codes.iloc[:, 0])
    # Відкидаємо порожні значення на кшталт 'nan', ''
    codes = codes[codes.notna() & (codes != "") & (codes.str.lower() != "nan")]
    return set(codes.tolist())

def read_excel_any(path: Path, skiprows: int) -> pd.DataFrame | None:
    """Пробуємо зчитати Excel із пропуском перших рядків; без заголовків (header=None).
       Якщо двигун не підтримує формат — повертаємо None (та дамо попередження).
    """
    try:
        if path.suffix.lower() == ".xlsb":
            # для .xlsb потрібен пакет pyxlsb: pip install pyxlsb
            return pd.read_excel(path, engine="pyxlsb", header=None, skiprows=skiprows)
        # для .xlsx/.xls/.xlsm спробуємо за замовчуванням
        return pd.read_excel(path, header=None, skiprows=skiprows)
    except Exception as e:
        print(f"[УВАГА] Не вдалося прочитати файл: {path.name} — {e}")
        return None

# ===== ОСНОВНИЙ ПРОЦЕС =====
def main():
    if not SRC_DIR.exists():
        raise FileNotFoundError(f"Не знайдено вхідну папку: {SRC_DIR}")
    if not CODES_XLSX.exists():
        raise FileNotFoundError(f"Не знайдено файл з кодами: {CODES_XLSX}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # 1) Зчитуємо перелік кодів
    codes_set = read_codes_list(CODES_XLSX)
    if not codes_set:
        raise ValueError("Список кодів порожній. Перевірте файл із кодами (колонка A).")

    print(f"Кодів у списку: {len(codes_set)}")

    # 2) Проходимося по всіх Excel-файлах у папці
    files = sorted([p for p in SRC_DIR.iterdir() if p.is_file() and p.suffix.lower() in EXCEL_EXTS])

    if not files:
        raise FileNotFoundError(f"У папці {SRC_DIR} не знайдено Excel-файлів із розширеннями: {', '.join(EXCEL_EXTS)}")

    combined = []
    reference_ncols = None

    for f in files:
        df = read_excel_any(f, skiprows=SKIP_ROWS)
        if df is None:
            continue  # вже попередили

        # Перевірка кількості колонок: мають збігатися за порядком
        if reference_ncols is None:
            reference_ncols = df.shape[1]
            if reference_ncols <= FILTER_COL_IDX:
                print(f"[УВАГА] У файлі {f.name} колонок менше ніж потрібно для фільтрації (потрібно >= {FILTER_COL_IDX+1}). Пропускаю.")
                continue
        else:
            if df.shape[1] != reference_ncols:
                print(f"[УВАГА] {f.name}: кількість колонок {df.shape[1]} ≠ очікуваних {reference_ncols}. Пропускаю файл, щоб не зіпсувати порядок.")
                continue

            if df.shape[1] <= FILTER_COL_IDX:
                print(f"[УВАГА] {f.name}: недостатньо колонок для фільтрації за L. Пропускаю.")
                continue

        # Фільтрація за колонкою L (індекс 11) на основі списку кодів
        to_filter = normalize_code_series(df.iloc[:, FILTER_COL_IDX])
        mask = to_filter.isin(codes_set)
        filtered = df[mask]

        if filtered.empty:
            print(f"[ІНФО] {f.name}: після фільтрації рядків немає.")
        else:
            combined.append(filtered)

        print(f"[OK] Опрацьовано: {f.name} | Вибрано рядків: {len(filtered)}")

    if not combined:
        raise ValueError("Після обробки усіх файлів не залишилося жодного рядка. Перевірте валідність кодів та колонку L у вхідних файлах.")

    result = pd.concat(combined, axis=0, ignore_index=True)

    # 3) Запис у один Excel без заголовків і без індексу
    out_path = OUT_DIR / OUT_NAME
    try:
        result.to_excel(out_path, index=False, header=False)
    except Exception as e:
        raise RuntimeError(f"Не вдалося зберегти результат у {out_path}: {e}")

    print(f"[ГОТОВО] Рядків у підсумку: {len(result)}")
    print(f"[ФАЙЛ] {out_path}")

if __name__ == "__main__":
    main()
