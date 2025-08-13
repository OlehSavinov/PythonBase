import numpy as np
import pandas as pd

# file name for input (in python path)
file = 'F:\Олег\СЗР_зерно\Pandas_transform\Input_file_zerno.xlsx'
df = pd.read_excel(file)

# Коефіціент базової одиниці (всі решта = 1)
coef = {'0.001': 'кг, кг містк'.split(', '),
        '0.1': 'ц'.split(', '),
        '1000': 'тис.т'.split(', '),
        }

def argcontains(item):
    for i, v in coef.items():
        if item in v:
            return float(i)

df['Коефіціент базової одиниці'] = df['Одиниця виміру'].map(argcontains).fillna(1)


# Культура
dir_codes = pd.read_excel('F:\Олег\СЗР_зерно\Справочники\Справочник продуктов зерно.xlsx', sheet_name='спрКоды')
dir_codes = dir_codes.astype({'Код УКТЗЕД': str}, errors='ignore')
df = df.astype({'Код УКТЗЕД': str}, errors='ignore')

df = pd.merge(df, dir_codes[['Код УКТЗЕД', 'Культура']], on='Код УКТЗЕД', how='left')
df = df.astype({'Культура': str, 'Номенклатура': str}, errors='ignore')

#not seeds
seeds_um = 'г, га, л, міш, од, п.е., п.о., п/о, пак, по., посад.місц, умов.од, умов.шт, шт'.split(', ')
df['Культура'] = np.where(df['Одиниця виміру'].isin(seeds_um), '0', df['Культура'])

seeds_nom = 'відход|гібр|круїз|LG|Відход'
df['Культура'] = np.where(df['Номенклатура'].str.contains(seeds_nom), '0', df['Культура'])

df['Культура'] = np.where(df['Код УКТЗЕД'].str.contains('110000'), '0', df['Культура'])


# Клас
df['Клас'] = df['Номенклатура'].str.replace(" ", "").str.extract('([1-6])[гк-][олг]')
df['Клас'] = np.where(df['Клас'].isna() & df['Номенклатура'].str.contains('вищ'), 'вищий', df['Клас'])
df['Клас'] = np.where(df['Клас'].isna() & df['Номенклатура'].str.contains('неклас'), 'некласний', df['Клас'])


# Урожай (рік)
df['Урожай (рік)'] = df['Номенклатура'].str.extract('(20[123]\d)')
df[['Клас', 'Урожай (рік)']] = df[['Клас', 'Урожай (рік)']].replace(r'^\s*$', np.nan, regex=True).fillna('Немає даних')


# Тест культури
df['Тест культури'] = [x[0] in x[1] for x in zip(df['Культура'].str[:3].str.lower(), df['Номенклатура'].str.lower())]


if __name__ == '__main__':
    df.to_excel('Output_file_zerno.xlsx', index=False)

