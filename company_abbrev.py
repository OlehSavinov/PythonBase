import re
import pandas as pd
from pathlib import Path

INPUT_PATH = Path(r"F:\Олег\Компанії\Input_company.xlsx")
OUTPUT_PATH = Path(r"F:\Олег\Компанії\Output_company.xlsx")

# Мапа замін: (повна назва статусу) -> (скорочення)
REPLACEMENTS = {
    "АКЦІОНЕРНЕ ТОВАРИСТВО": "АТ",
    "ПРИВАТНЕ АКЦІОНЕРНЕ ТОВАРИСТВО": "ПрАТ",
    "ТОВАРИСТВО З ОБМЕЖЕНОЮ ВІДПОВІДАЛЬНІСТЮ": "ТОВ",
    "СІЛЬСЬКОГОСПОДАРСЬКЕ ТОВАРИСТВО З ОБМЕЖЕНОЮ ВІДПОВІДАЛЬНІСТЮ": "СТОВ",
    "ПРИВАТНЕ СІЛЬСЬКОГОСПОДАРСЬКЕ ПІДПРИЄМСТВО": "ПСП",
    "СЕЛЯНСЬКЕ (ФЕРМЕРСЬКЕ) ГОСПОДАРСТВО": "СФГ",
    "ФЕРМЕРСЬКЕ ГОСПОДАРСТВО": "ФГ",
    "СІЛЬСЬКОГОСПОДАРСЬКА ФІРМА": "СФ",
    "МАЛЕ ПРИВАТНЕ ПІДПРИЄМСТВО": "МПП",
    "ПРИВАТНЕ ВИРОБНИЧО -КОМЕРЦІЙНЕ ПІДПРИЄМСТВО": "ПВКП",
    "СІЛЬСЬКОГОСПОДАРСЬКЕ ПІДПРИЄМСТВО": "СП",
    "ДОЧІРНЄ ПІДПРИЄМСТВО": "ДП",
    "ПРИВАТНЕ ПІДПРИЄМСТВО": "ПП",
    "ДЕРЖАВНЕ ПІДПРИЄМСТВО": "ДП",
    "ПУБЛІЧНЕ АКЦІОНЕРНЕ ТОВАРИСТВО": "ПАТ",
    "КОМУНАЛЬНЕ ПІДПРИЄМСТВО": "КП",
    "ТОВАРИСТВО З ДОДАТКОВОЮ ВІДПОВІДАЛЬНІСТЮ": "ТДВ",
    "ВИРОБНИЧО - КОМЕРЦІЙНА ФІРМА": "ВКФ"
}

# Мапа символів
LATIN_TO_CYRILLIC = str.maketrans({
    "A": "А", "B": "В", "C": "С", "E": "Е", "H": "Н",
    "I": "І", "K": "К", "M": "М", "O": "О", "P": "Р",
    "T": "Т", "X": "Х",
})



# --- Нормалізація: прибираємо дужки/лапки/дефіси/тире та зайві пробіли, верхній регістр ---
# Логіка така: і назву, і ключі мапи приводимо до однакового "плоского" виду,
# а заміну робимо regex-ом у вихідному тексті, ігноруючи "шум" між словами.
NOISE_CHARS_RE = re.compile(r"[\"'`«»“”‘’.,;:!?\[\]{}<>/\\|_]+")
DASHES_RE = re.compile(r"[‐-‒–—−-]+")  # різні дефіси/тире
BRACKETS_RE = re.compile(r"[()]+")
MULTISPACE_RE = re.compile(r"\s+")

def normalize_for_match(s: str) -> str:
    if s is None:
        return ""
    s = str(s).upper()
    s = s.translate(LATIN_TO_CYRILLIC)  # латинські двійники -> кирилиця
    s = BRACKETS_RE.sub(" ", s)
    s = DASHES_RE.sub(" ", s)
    s = NOISE_CHARS_RE.sub(" ", s)
    s = MULTISPACE_RE.sub(" ", s).strip()
    return s


def build_fuzzy_phrase_pattern(phrase: str) -> re.Pattern:
    """
    Будує патерн, який шукає слова фрази по порядку, але дозволяє між ними будь-який "шум":
    пробіли, дужки, тире, лапки тощо.
    """
    words = normalize_for_match(phrase).split()
    # між словами дозволимо будь-що з "не-літер/цифр" + пробіли
    sep = r"(?:[\s()\"'`«»“”‘’.,;:!?\-‐-‒–—−/_\\|]*)"
    # межі слова: не літера/цифра або початок/кінець
    left = r"(?:(?<=^)|(?<=[^\wА-ЯІЇЄҐ0-9]))"
    right = r"(?:(?=$)|(?=[^\wА-ЯІЇЄҐ0-9]))"
    body = sep.join(map(re.escape, words))
    return re.compile(left + body + right, flags=re.IGNORECASE)

# Готуємо список замін: довші фрази — першими
items = sorted(REPLACEMENTS.items(), key=lambda kv: len(normalize_for_match(kv[0]).split()), reverse=True)

# Для швидкості: зберігаємо зкомпільовані патерни
compiled = [(build_fuzzy_phrase_pattern(full), short) for full, short in items]

def shorten_company_name(name: str) -> str:
    if name is None or (isinstance(name, float) and pd.isna(name)):
        return name
    text = str(name)

    # робимо заміни у вихідному тексті (збережемо решту назви як є)
    for pat, short in compiled:
        text = pat.sub(short, text)

    # косметика: прибрати "подвійні" пробіли після замін
    text = MULTISPACE_RE.sub(" ", text).strip()
    return text

def main():
    df = pd.read_excel(INPUT_PATH, engine="openpyxl")

    if "Назва" not in df.columns:
        raise ValueError("У файлі немає колонки 'Назва'.")

    df["Назва скорочена"] = df["Назва"].apply(shorten_company_name)

    df.to_excel(OUTPUT_PATH, index=False, engine="openpyxl")
    print(f"Готово: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
