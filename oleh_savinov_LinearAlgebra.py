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


# 5. Вывести матрицу, которая при умножении на вектор слева (Мх) приводит его к форме отклонения от среднего значения.
# То есть каждым элементом вектора-результата будет соответствующий элемент входящего вектора минус среднее значение.
# Матрица М не должна зависеть от входящего вектора х, а только от его длины.
# Другими словами, для создания такой матрицы должно быть достаточно только знания сколько в х элементов.

def generate_M(n):
    M = np.eye(N=n) + np.ones(shape=(n, n)) * (-1 / n)
    return M

# np.set_printoptions(precision=4, suppress=True)
# A = np.random.randint(0, 5, (6, 1))
# print(A)
# print(generate_M(A.shape[0]).dot(A))


# 6. Решить систему уравнений (можно воспользоваться функцией извлечения корня):

b = np.array([3, 3, 24])
A = np.array([
    [47, 71, -2],
    [0, 11, -8],
    [1, 1, 1]
])
x = np.linalg.inv(A).dot(b)
a, b, c = np.sqrt(x[0]), x[1], x[2]
print(a, b, c)