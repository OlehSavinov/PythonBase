import pandas as pd
import numpy as np

titanic_data = pd.read_csv('TitanicDataset.csv', sep=',', header=0)
# print(titanic_data.head())


# 2. Создать колонку, которая содержит фамилию пассажира и приписку 'above average', если он старше среднего возраста
# (среди всех пассажиров) и 'below average' если наоборот. Пример: 'William, below average'

td_fil = titanic_data[~titanic_data['Age'].isna()].copy()
avg_age = np.mean(td_fil['Age'])
age_category = np.where(td_fil['Age'] > avg_age, 'above average', 'below average')
td_fil['Lastname_age'] = td_fil['Name'].apply(lambda x: f"{x.split(',')[0]}, {age_category}", axis = 1)
print(td_fil[['Age', 'Lastname_age']].head(15))