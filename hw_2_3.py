def count_fib(x):
    global fib1
    global fib2
    count = 0
    print('Ряд следующих чисел:', end=' ')
    while count < int(n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        count += 1
        if count == int(n):
            print(fib)
        else:
            print(fib, end = ', ')

print ('Первые Числа Фибоначчи: 1, 1')
n = '1'
fib1 = 1
fib2 = 1
while n:
    n = input('Введите количество следующих Чисел Фибоначчи: ')
    if n.isdigit() and n != '0':
        count_fib(int(n))
    else:
        exit()
