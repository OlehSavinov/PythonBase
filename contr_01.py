def square(a, b):
    print('square', '(', a, ', ', b, ')')
    print('*' * a)
    for i in range(b - 2):
        print('*', end = '')
        print(' ' * (a - 2), end = '')
        print('*')
    print('*' * a)


square(5, 8)
