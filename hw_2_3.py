def count_fib(x):
    global n
    fib1 = 1
    fib2 = 1
    count = 0
    print('Ряд:', end = ' ')
    while count < n:
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        count += 1
        if count == n:
            print(fib)
        else:
            print(fib, end = ', ')


print ('Первые Числа Фибоначчи: 1, 1')
n = '1'
while n.isdigit() and n != '0':
    n = input('Введите количество следующих Чисел Фибоначчи: ')
    n = int(n)
    count_fib(n)
else:
    exit()

# n = input('Введите количество следующих Чисел Фибоначчи: ')
# if n.isdigit() and n != '0':
#     count_fib(int(n))
# else:
#     exit()
