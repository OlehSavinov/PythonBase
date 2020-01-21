def sum_of_natural_numbers(a, b):
    res = 0
    if float(a) < float(b):
        a = float_1(a)
        b = float_2(b)
        for i in range(a, b + 1):
            res += i
    elif float(a) == float(b):
        if a.isdigit():
            res = a
        else:
            res = 0
    else:
        a = float_2(a)
        b = float_1(b)
        for i in range(b, a + 1):
            res += i
    return res

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def float_1(a):
    if a.isdigit():
        a = int(a)
    elif float(a) < 0:
        a = 0
    else:
        a = int(float(a) // 1) + 1
    return a

def float_2(a):
    if float(a) < 0:
        a = 0
    else:
        a = int(float(a) // 1)
    return a

rep = 'Y'
while not rep in 'NnНн':
    if rep in 'YyДд':
        a = ''
        while not isfloat(a):
            a = input('Введите число a: ')
            if a == 'выход':
                print('Вы вышли из программы')
                exit()

        b = ''
        while not isfloat(b):
            b = input('Введите число b: ')
            if b == 'выход':
                print('Вы вышли из программы')
                exit()

        print('Результат суммы натуральных чисел в указанном диапазоне:', sum_of_natural_numbers(a, b), '\n')
    rep = input('Повторить? Для продолжения введите символ Y/y/Д/д; Для выхода введите символ N/n/Н/н: ')
