import pandas as pd
import re

# Шляхи до файлів (Windows)
input_nom_path = r'F:\Олег\Сельхозтехника\Input_nom_SGT.xlsx'
ref_path = r'F:\Олег\СЗР\Справочники\Справочник продуктов.xlsx'
output_path = r'F:\Олег\Сельхозтехника\Output_nom_SGT.xlsx'

# ------------------------ допоміжні функції ------------------------
def clean_code(x):
    """Нормалізує код УКТЗЕД/УКТЗЕД до рядка з цифр без пробілів та розділювачів."""
    s = str(x) if pd.notna(x) else ''
    s = re.sub(r'[^0-9]', '', s)
    return s

replacements = {'й':'ї','и':'і','мега':'mega'}

def normalize_and_replace(text):
    """
    Нормалізація для пошуку:
    - lower;
    - автозаміни;
    - прибираємо зайві символи;
    - ВАЖЛИВО: видаляємо УСІ пробіли та коми/крапки (щоб 'Maestro 24SW' ~ 'Maestro 24 SW').
    """
    s = str(text).lower()
    s = re.sub(r'[-–—]', ' ', s)
    for wrong, correct in replacements.items():
        s = s.replace(wrong, correct)
    s = re.sub(r'[^0-9a-zа-яіїєґ\+\*/\/,\.× ]', '', s)
    s = re.sub(r'\s+', '', s)
    s = s.replace(',', '').replace('.', '')
    return s

def strip_brand_prefix(name, brand):
    """Вирізає бренд на початку 'Загальна назва' (нечутливо до регістру)."""
    if pd.isna(name) or pd.isna(brand):
        return name
    pattern = r'^\s*' + re.escape(str(brand)).strip() + r'[\s\-:]*'
    return re.sub(pattern, '', str(name), flags=re.IGNORECASE)

# ------------------------ 1) Вхідні дані ------------------------
df_nom = pd.read_excel(input_nom_path, sheet_name='номенклатура')

# Визначаємо назву колонки з кодом УКТЗЕД у вхідному файлі
code_col_candidates = ['Код УКТЗЕД', 'Тип УКТЗЕД']
code_col = next((c for c in code_col_candidates if c in df_nom.columns), None)
if code_col is None:
    raise KeyError("У файлі Input очікується колонка 'Код УКТЗЕД' або 'Тип УКТЗЕД'.")

df_nom['_code_norm'] = df_nom[code_col].apply(clean_code)

# ------------------------ 2) Довідники ------------------------
# 2.1 «спрКоды»: Код УКТЗЕД → Культура
df_kody = pd.read_excel(ref_path, sheet_name='спрКоды')
if not {'Код УКТЗЕД', 'Культура'}.issubset(df_kody.columns):
    raise KeyError("У листі 'спрКоды' повинні бути колонки 'Код УКТЗЕД' і 'Культура'.")
df_kody['_code_norm'] = df_kody['Код УКТЗЕД'].apply(clean_code)
df_kody = df_kody[['Культура', '_code_norm']].drop_duplicates()

# 2.2 «спрПродукти_СГТ»: довідник продуктів
df_ref_raw = pd.read_excel(ref_path, sheet_name='спрПродукти_СГТ')
required_cols = {'Загальна назва', 'Внутрішній код', 'Субкатегорія', 'Бренд'}
missing = required_cols - set(df_ref_raw.columns)
if missing:
    raise KeyError(f"У листі 'спрПродукти_СГТ' відсутні колонки: {sorted(missing)}")

# --- НОВЕ: фільтр за «небажаними» підрядками у 'Загальна назва'
bad_substrings = [
    "агрегат","аератор","асенізац","борон","бункер","буртоукл","буряко","викорч","візок","газонокос",
    "гичкозб","глибокороз","грабл","грядкоут","грунтофрез","дощувал","екскаватор","навантажувач","жнивар",
    "зворушувач","зерносуш","змішувач","зчіпн","картоплек","каток","комбайн","копалк","кормозм","кормороз",
    "корчувач","косарк","культиватор","переробк","розрізан","міксер","молотарк","мотоблок","мульчувач","дрон",
    "обертач","компост","обмотувал","обприскувач","обрізувач","очисн","підрізчик","плуг","подрібн","підбирач",
    "пересадк","причеп","причіп","протруювач","розкидач","розпушувач","саджалк","зрошен","системонос","сівалк",
    "скарифікатор","сортувал","трактор","ущільнювач","фреза","цистерн"
]

# НЕзахоплююча група (?:...) + ігнор регістру
pattern_bad = re.compile(r'(?:' + '|'.join(map(re.escape, bad_substrings)) + r')', flags=re.IGNORECASE)

# тепер без попередження
mask_bad = df_ref_raw['Загальна назва'].astype(str).str.contains(pattern_bad, na=False)
removed_count = int(mask_bad.sum())
df_ref_raw = df_ref_raw[~mask_bad].copy()

print(f"Видалено рядків за стоп-словами: {removed_count}")


# --- Вирізання бренду на початку назви (перед аналізом)
df_ref_raw['Назва_для_аналізу'] = df_ref_raw.apply(
    lambda r: strip_brand_prefix(r['Загальна назва'], r['Бренд']),
    axis=1
)

# --- Попереднє сортування за довжиною очищеної назви (від більшої до меншої)
df_ref_raw = df_ref_raw.sort_values(
    'Назва_для_аналізу',
    key=lambda s: s.astype(str).str.len(),
    ascending=False
).reset_index(drop=True)

# ------------------------ 3) Матчимо Культуру до номенклатури ------------------------
df_nom = df_nom.merge(df_kody, on='_code_norm', how='left')  # додаємо 'Культура'

# ------------------------ 4) Підготовка довідника ------------------------
df_ref = df_ref_raw[['Назва_для_аналізу', 'Внутрішній код', 'Субкатегорія']].copy()

norm_len = (df_ref['Назва_для_аналізу'].astype(str)
            .str.replace(r"[^0-9a-zA-Zа-яА-Яіїєґ]+", '', regex=True)
            .str.len())
df_ref = df_ref[norm_len >= 4]

codes_to_remove = ['TMOT-000536', 'TPPI-000012', 'TKKO-000061', 'TKOM-000013', 'TKZE-000024', 'TMOT-000524',
                   'TGAZ-000009', 'TBDI-000687', 'TOBP-000330', 'TBDI-000090', 'TKUL-000097']
df_ref = df_ref[~df_ref['Внутрішній код'].isin(codes_to_remove)].reset_index(drop=True)

# Нормалізована назва (без пробілів, у lower) для substring-пошуку
df_ref['norm_name'] = df_ref['Назва_для_аналізу'].apply(normalize_and_replace)

# Індекс за субкатегоріями (усередині вже відсортовано за довжиною ↓)
cat_to_ref = {
    cat: sub_df[['Внутрішній код', 'norm_name']].reset_index(drop=True)
    for cat, sub_df in df_ref.groupby('Субкатегорія', sort=False)
}
# Глобальний список для fallback-пошуку по інших субкатегоріях
df_ref_all = df_ref[['Внутрішній код', 'norm_name', 'Субкатегорія']].reset_index(drop=True)

# ------------------------ 5) Пошук у 2 етапи ------------------------
def match_code_two_stage(nom_text, allowed_category):
    """
    Етап 1: шукаємо тільки в allowed_category.
    Етап 2 (fallback): якщо не знайшли — шукаємо по інших субкатегоріях.
    Нормалізація номенклатури: без пробілів + lower, щоб 'Maestro 24SW' ~ 'Maestro 24 SW'.
    """
    search = normalize_and_replace(nom_text)

    # Етап 1 — всередині категорії
    if pd.notna(allowed_category):
        sub = cat_to_ref.get(str(allowed_category))
        if sub is not None and not sub.empty:
            for _, row in sub.iterrows():
                if row['norm_name'] and row['norm_name'] in search:
                    return row['Внутрішній код']

    # Етап 2 — по інших категоріях
    for _, row in df_ref_all.iterrows():
        if pd.notna(allowed_category) and str(row['Субкатегорія']) == str(allowed_category):
            continue
        if row['norm_name'] and row['norm_name'] in search:
            return row['Внутрішній код']

    return None

# ------------------------ 6) Застосування до номенклатури ------------------------
df_nom['Внутрішній код'] = [
    match_code_two_stage(nm, cat)
    for nm, cat in zip(df_nom['Номенклатура'], df_nom['Культура'])
]

# ------------------------ 7) Фінальне впорядкування та збереження ------------------------
cols = df_nom.columns.tolist()
if 'Номенклатура з одиницею виміру' in cols:
    cols.remove('Номенклатура з одиницею виміру')
    df_nom = df_nom[['Номенклатура з одиницею виміру'] + cols]

# Приберемо службову колонку
df_nom = df_nom.drop(columns=['_code_norm'])

with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_nom.to_excel(writer, sheet_name='номенклатура', index=False)

print('Готово! Результат збережено в', output_path)
