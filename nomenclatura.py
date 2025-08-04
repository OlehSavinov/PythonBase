import pandas as pd
import re
import os

# Шляхи до файлів (Windows)
input_nom_path = r'F:\Олег\ЗЗР\Input_nom_zzrd.xlsx'
ref_path = r'F:\Олег\СЗР\Справочники\Справочник продуктов.xlsx'
output_path = r'F:\Олег\ЗЗР\Output_nom_zzrd.xlsx'

# 1) Зчитуємо номенклатуру та добрива з колонками "Номенклатура з одиницею виміру", "Номенклатура", "Одиниця виміру"
df_nom = pd.read_excel(input_nom_path, sheet_name='номенклатура')

# 2) Зчитуємо довідник продуктів та фільтруємо за категоріями ЗЗР і Добрива
df_ref = pd.read_excel(ref_path, sheet_name='спрПродукты')
df_ref = df_ref[df_ref['Категорія'].isin(['ЗЗР', 'Добрива'])][['Загальна назва', 'Внутрішній код']]

# 3) Розбиваємо записи з '/' у довіднику на окремі рядки
ref_expanded = []
for _, row in df_ref.iterrows():
    for part in str(row['Загальна назва']).split('/'):
        new_row = row.copy()
        new_row['Загальна назва'] = part.strip()
        ref_expanded.append(new_row)
df_ref = pd.DataFrame(ref_expanded)

# 4) Фільтрація довідника: назви >=4 символів та виняткові коди
norm_len = (df_ref['Загальна назва'].astype(str)
            .str.replace(r"[^0-9a-zA-Zа-яА-ЯіїєґІЇЄҐ]+", '', regex=True)
            .str.len())
df_ref = df_ref[norm_len >= 4]
codes_to_remove = [
    'PREG-000157','PFUN-000575','PGER-000136','PGER-000122','PFUN-000336',
    'PREG-000137','PFUN-000144','PFUN-000190','PGER-001029','PPRT-000164',
    'PGER-000893','PREG-000022','PGER-000982','PGER-000361','PPRT-000047',
    'PROD-000027','PPAR-000010','PDES-000002','PPAR-000005','PAAA-000001',
    'PPAR-000129','PFUN-000564','PINS-000386','PINS-000473','PPAR-000053',
    'PROD-000063','PGER-000573','PFUN-000119','PGER-000440','PINK-000022',
    'PPAR-000111','DMPO-001841','PGER-000005','PGER-000562','PFUN-000350',
    'PPAR-000255','PGER-000373','PINS-000314','PGER-000803','DMPO-001278',
    'PGER-000998','PROD-000064','PGER-000680','DMPO-001910','DMPO-001617',
    'PREG-000179','PREG-000116','DMPO-000712','PGER-001458','PGER-000578',
    'PREG-000118','DMPO-000853','PINK-000085','PFUN-000578','PGER-000131',
    'PGER-001098','PGER-000330','PINS-000185','PPRT-000179','PPRT-000113',
    'DMPO-001268','PFUN-000412','PPAR-000033','PINS-000510','PGER-000017',
    'DMPO-000241','PGER-001221','DMPO-000884','PFUN-000821','PINK-000059',
    'PGER-001492','PINS-000506','DMPO-000686','DMPO-000893','PGER-001078',
    'PINS-000398','DMPO-001410','DNPK-000094','PGER-001355','PPRT-000123',
    'DMPO-001875','PGER-000888','DMIN-000284','DMPO-001862','PDES-000005',
    'DMIN-000327','PGER-000019','PGER-000845','PREG-000007','DMIN-000258',
    'DNPK-000078','DMMO-000322','PGER-000784','DMPO-002439','PGER-001293',
    'DMPO-000733','DMPO-001056','PGER-001528'
]
df_ref = df_ref[~df_ref['Внутрішній код'].isin(codes_to_remove)]

# 5) Автозаміни для нормалізації тексту
dependencies = {
    'й': 'ї','и': 'і','фф': 'ф','ал': 'ап','max': 'макс',
    'ват': 'вант','e': 'є','raiza': 'райза','э': 'е',
    'i': 'і','c': 'с','t': 'т','x': 'х','фитолекарь': 'фітолікар',
    'калійхлористий': 'kcl','яравітабортрак': 'yaravitabortrac','інтермаг': 'intermag','пп': 'п',
    'квантум': 'quantum','гуміфілд': 'humifield','нутрімікс': 'nutrimix'
}

def normalize_and_replace(text):
    s = str(text).lower()
    for wrong, correct in dependencies.items():
        s = s.replace(wrong, correct)
    # Залишаємо літери, цифри, пробіли, '+' та '/'
    return re.sub(r'[^0-9a-zа-яіїєґ+\/ ]', '', s)

# 6) Підготовка довідника
df_ref['norm_name'] = df_ref['Загальна назва'].apply(normalize_and_replace)
df_ref = df_ref.assign(name_len=df_ref['norm_name'].str.len()).sort_values('name_len', ascending=False)

# 7) Підбір внутрішнього коду
def match_code(nom_text):
    desc_norm = normalize_and_replace(nom_text)
    for _, row in df_ref.iterrows():
        if row['norm_name'] and row['norm_name'] in desc_norm:
            return row['Внутрішній код']
    return None

# 8) Налаштування коефіцієнтів базової одиниці
unit_map = {
    1: {'л','кг','кл','літр','кілограмм','литр','k'},
    1000: {'т','тн','тисл','ттовпрод','ттовпродукт','м3','тонна','n','твантажопідйом','тмістк','тона','кубметр'},
    0.001: {'г','мл','гр'},
    100: {'ц'},
    1000000: {'тист'},
    0.5: {'05кг'},
    0.000001: {'мг'}
}

def calc_coeff(nom_text, unit_text):
    u = str(unit_text).lower().replace(' ', '')
    for coeff, units in unit_map.items():
        if u in units:
            return coeff
    text_norm = str(nom_text).lower()
    for wrong, correct in dependencies.items():
        text_norm = text_norm.replace(wrong, correct)
    for coeff, units in unit_map.items():
        for unit in units:
            pattern = rf"(?<!\d)(\d+[.,]?\d*)\s*{re.escape(unit)}(?!/)"
            m = re.search(pattern, text_norm)
            if m:
                num = float(m.group(1).replace(',', '.'))
                return num * coeff
    return None

def calc_pack_liters(nom_text):
    text_norm = str(nom_text).lower()
    for wrong, correct in dependencies.items():
        text_norm = text_norm.replace(wrong, correct)
    for coeff, units in unit_map.items():
        for unit in units:
            pattern = rf"(?<!\d)(\d+[.,]?\d*)\s*{re.escape(unit)}(?!/)"
            m = re.search(pattern, text_norm)
            if m:
                num = float(m.group(1).replace(',', '.'))
                return num * coeff
    return None

# 9) Застосування функцій до DF
df_nom['Внутрішній код'] = df_nom['Номенклатура'].apply(match_code)
df_nom['Коефіцієнт базової одиниці'] = df_nom.apply(lambda r: calc_coeff(r['Номенклатура'], r.get('Одиниця виміру', '')), axis=1)
df_nom['Фасування у літрах'] = df_nom['Номенклатура'].apply(calc_pack_liters)
df_nom['Дрібне фасування'] = df_nom['Фасування у літрах'].apply(lambda x: 1 if x is not None and x < 0.1 else None)

# 10) Перенесення колонки “Номенклатура з одиницею виміру” в початок та збереження
cols = df_nom.columns.tolist()
if 'Номенклатура з одиницею виміру' in cols:
    cols.remove('Номенклатура з одиницею виміру')
    df_nom = df_nom[['Номенклатура з одиницею виміру'] + cols]
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    df_nom.to_excel(writer, sheet_name='номенклатура', index=False)
print('Готово! Результат збережено в', output_path)
