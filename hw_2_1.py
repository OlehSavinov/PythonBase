def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

a = ''
while not isfloat(a) or a == '0':
    a = input('Введите коэффициент a (вещественное число, не равное нулю): ')
    if a == 'выход':
        print('Вы вышли из программы')
        exit()
a = float(a)

b = ''
while not isfloat(b):
    b = input('Введите коэффициент b (вещественное число): ')
    if b == 'выход':
        print('Вы вышли из программы')
        exit()
b = float(b)

c = ''
while not isfloat(c):
    c = input('Введите коэффициент c (вещественное число): ')
    if c == 'выход':
        print('Вы вышли из программы')
        exit()
c = float(c)

d = b ** 2 - 4 * a * c
print('-' * 60)

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Уравнение имеет два вещественных корня: x1 =', x1, 'x2 =', x2)
elif d == 0:
    x = -b / (2 * a)
    print('Уравнение имеет один корень:', x)
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print('Уравнение не имеет вещественных корней. Комплексные корни: x1 =', x1, 'x2 =', x2)
