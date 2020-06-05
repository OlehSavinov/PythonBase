import numpy as np

# 1. Дано: одномерный массив
# Задача: заменить все элементы этого массива, которые больше среднего на среднее значение

arr = np.random.rand(1000)
res = np.where(arr > np.mean(arr), np.mean(arr), arr)
# print(res)


# 2. Для массива из предыдущей задачи имплементировать сигмоид функцию

sigm = 1 / (1 + np.exp(-res))
print(sigm)