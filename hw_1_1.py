ns = input('Введите имя и фамилию:')
print('Здравствуйте,', ns)

d = int(input('\nВведите дату рождения (день):'))
m = int(input('Введите месяц рождения (числом):'))
y = int(input('Введите год рождения:'))

# вычисление по состоянию на 16.01.2020 (с погрешностью)
q_y_today = ((2019 - y) * 365 + (12 - m) * 30 + (30 - d) + 16) // 365
q_m_today = ((2019 - y) * 365 + (12 - m) * 30 + (30 - d) + 16) // 30
print('-' * 60)
print('Количество прожитых лет:', q_y_today)
print('Количество прожитых месяцев:', q_m_today)

# вычисление на дату начала курса 10.01.2020 (с погрешностью)
q_y_course = ((2019 - y) * 365 + (12 - m) * 30 + (30 - d) + 10) // 365
q_m_course = ((2019 - y) * 365 + (12 - m) * 30 + (30 - d) + 10) // 30
q_d_course = ((2019 - y) * 365 + (12 - m) * 30 + (30 - d) + 10)
print('Прожито до начала курса:', q_d_course, 'дней,', q_m_course, 'месяцев,', q_y_course, 'лет')
