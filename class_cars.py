'''
Создайте класс, описывающий автомобиль.
Создайте класс, описывающий салон автомобилей в котором имеется:
    ➢ Атрибут «перечень автомобилей»
    ➢ Атрибут «выручка»
    ➢ Метод «продажа автомобиля»
    ➢ Метод «услуга покраски автомобиля»
'''

reg_id = 1

class Car:
    def __init__(self, price=0.0, color='black', model_name='Ford', vin=''):
        self.price = price
        self.color = color
        self.vin = vin
        self.model_name = model_name

        global reg_id
        reg_id += 1
        self.id = reg_id

    def __str__(self):
        return f"{self.id}:{self.model_name}(vin={self.vin}){self.price} {self.color}"
car1 = Car()
car1.rice = 10
car1.color = 'white'

car2 = Car(11, 'cyam')

car3 = Car(10, 'white')


# print(car1.price, car2, car3, sep='\n')
# print(car1, car2, car3, sep='\n')

class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []  # Перечень автомобилей в салоне
        self.profit = 0.0

    def __str__(self):
        return f"{self.name}"

    def append(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"'Ожидается тип 'Car', а получен {type(car)}'")
        self.cars.append(car)

salon1 = AutoSalon('АВТ_Бавария')

print(salon1)