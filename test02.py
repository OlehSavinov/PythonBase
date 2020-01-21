def divide(x, y, printing=False):
    def print_result(val):
        if val is None:
            print('Деление на 0 запрещено!')
        else:
            print('Результат деления =', val)

    val = 'sdfsdfgsdfgsdgdf'
    if y == 0:
        result = None
    elif isinstance(x, int) and isinstance(y, int):
        result = x // y
    else:
        result = x / y
    if printing:
        print_result(result)
    return result


print(divide(5, 2))
divide(5, 2, True)
divide(5, 2, printing=True)
print(divide(1, 0))
divide(1, 0, True)