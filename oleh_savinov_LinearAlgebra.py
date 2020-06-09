import numpy as np

# 2. Для вектора из предыдущей задачи построить вектор, каждым элементом которого является среднее значение вектора.
v = np.array([1, 2, 3, 4, 5, 6])
avg_v = v.dot(np.ones_like(v)) / v.shape
res = np.ones_like(v) * avg_v
# print(res)


# 3. Написать функцию, которая принимает на вход произвольное количество матриц, проверяет можно ли их перемножить,
# и если можно, то возвращает размерность результата (можно воспользоваться циклом).
def matrix_dim(*args):
    for i in range(len(args)-1):
        if args[i].shape[1] == args[i+1].shape[0]:
            return args[i].dot(args[i+1])
        else:
            return False
A = np.random.randint(0, 5, (3, 2))
B = np.random.randint(0, 5, (2, 3))
print(A)
print(B)
print(matrix_dim(A, B))