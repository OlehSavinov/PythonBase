import numpy as np

# 1. Дано: одномерный массив
# Задача: заменить все элементы этого массива, которые больше среднего на среднее значение

arr = np.random.rand(1000)
res = np.where(arr > np.mean(arr), np.mean(arr), arr)
# print(res)


# 2. Для массива из предыдущей задачи имплементировать сигмоид функцию

sigm = 1 / (1 + np.exp(-res))
# print(sigm)


# 3. Решить задачу про таблицу сотрудников используя numpy (вывести на экран можно без форматирования)

workers_table = np.array([
    [1, 'B', 1000, 2013],
    [2, 'B', 1500, 2014],
    [3, 'B', 1800, 2012],
    [4, 'A', 2500, 2016],
    [5, 'A', 3500, 2017],
    [6, 'A', 4500, 2011],
], dtype=np.object)

mask = np.array([workers_table[i][3] > 2012 and workers_table[i][2] > 2000 for i in range(len(workers_table))])
res3 = workers_table[mask]
# print(res3)


# 4. Дана таблица A
# Задача - нормализовать колонки (сделать так, чтобы длина векторов в колонках была 1)

A = np.array([
    [2, 5, 8, 56],
    [4, 9, 1, 23],
    [6, 12, 84, 55]
])

norm_tab = A * (1 / np.sqrt(np.sum(A ** 2, axis=0)))
# print(norm_tab)
