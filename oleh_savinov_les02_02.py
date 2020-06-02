# 1. Написать функцию, которая генерирует последовательность из n чисел Фибоначчи (n принимается как аргумент).
# Воспользоваться оператором "yield"
def fibonach(n):
    fib1 = 0
    fib2 = 1
    yield 1
    for i in range(n-1):
        fib = fib1 + fib2
        yield fib
        fib1 = fib2
        fib2 = fib

