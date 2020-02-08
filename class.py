class Car:
    def __init__(self, brand, model, body_type, fuel_cons):
        self.brand = brand
        self.model = model
        self.body_type = body_type
        self.fuel_cons = fuel_cons

    def print_car(self):
        print(f"Название бренда: {self.brand}\nМодель: {self.model}\nТип кузова: {self.body_type}\nРасход топлива: {self.fuel_cons}")

renault = Car('Рено', 'Кенго', 'фургон', 7.9)
res = renault.print_car()
print(res)


class Car_salon:
    