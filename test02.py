x = int(input('Введите максимальное значение счётчика: '))
for i in range(x+1):
    if i < 2:
        continue
    elif i > 5:
        break
    else:
        print(i)
# else:
if i == x:
    print('Достигли конца цикла нормальным путём (Else)')
