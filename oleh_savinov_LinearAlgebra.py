import numpy as np

# 2. Для вектора из предыдущей задачи построить вектор, каждым элементом которого является среднее значение вектора.

v = np.array([1, 2, 3, 4, 5, 6])
avg_v = v.dot(np.ones_like(v)) / v.shape
res = np.ones_like(v) * avg_v
# print(res)


# 3. Написать функцию, которая принимает на вход произвольное количество матриц, проверяет можно ли их перемножить,
# и если можно, то возвращает размерность результата (можно воспользоваться циклом).

def matrix_dim(*args):
    if len(args) == 1:
        print('Для перемножения введите хотя бы две матрицы')
        return None
    for i in range(len(args)-1):
        if args[i].shape[1] != args[i+1].shape[0]:
            print('Матрицы перемножить нельзя')
            break
    else:
        print('Размерность результирующей матрицы:')
        return args[0].shape[0], args[-1].shape[1]

# A = np.random.randint(0, 5, (8, 5))
# B = np.random.randint(0, 5, (5, 10))
# C = np.random.randint(0, 5, (10, 5))
# D = np.random.randint(0, 5, (5, 2))
# print(A.dot(B).dot(C).dot(D))
# print(matrix_dim(A, B, C, D))


# 4. Вычислить выражение:

def res_expression(x):
    v = x.reshape(1, x.shape[0] * x.shape[1])
    avg = v.dot(np.ones_like(v).T) / v.shape[1]
    avg_m = np.ones_like(v) * avg
    dif = v - avg_m
    res = dif.dot(dif.T)
    return res

# A = np.random.randint(0, 5, (1, 7))
# print(A)
# print(res_expression(A))