import pandas as pd
import numpy as np

titanic_data = pd.read_csv('TitanicDataset.csv', sep=',', header=0)
# print(titanic_data.head())


# 2. Создать колонку, которая содержит фамилию пассажира и приписку 'above average', если он старше среднего возраста
# (среди всех пассажиров) и 'below average' если наоборот. Пример: 'William, below average'

td_fil = titanic_data[~titanic_data['Age'].isna()].copy()
avg_age = np.mean(td_fil['Age'])
td_fil['Lastname_age'] = td_fil['Name'].apply(lambda x: x.split(',')[0]) + ', ' \
                         + np.where(td_fil['Age'] > avg_age, 'above average', 'below average')
# print(td_fil[['Age', 'Lastname_age']].head())


# 3. Найти среднюю, минимальную и максимальную стоимость билета в зависимости от места посадки и класса каюты

res = titanic_data.groupby(by=['Embarked', 'Pclass']).agg(
    mean_fare = ('Fare', np.mean),
    min_fare = ('Fare', np.min),
    max_fare = ('Fare', np.max)
)
# print(res)


# 4. Найти всех родственников по фамилии. В результате должна получиться таблица с 2-мя колонками.
# В первой колонке полное имя пассажира, во второй всех его родственников на борту.

titanic_data['Lastname'] = titanic_data['Name'].apply(lambda x: x.split(',')[0])
titanic_data_F = titanic_data.rename(
    columns={
        'PassengerId': 'PassengerId_F',
        'Name': 'Family',
    },
    inplace=False
)
merged_data = pd.merge(
    left=titanic_data[['PassengerId', 'Name', 'Lastname']],
    right=titanic_data_F[['PassengerId_F', 'Family', 'Lastname']],
    on='Lastname',
    how='inner'
)
res_table = merged_data[merged_data['PassengerId'] != merged_data['PassengerId_F']]
# print(res_table[['Name', 'Family']].head(50))
