# 1. Создать класс Car, в конструкторе определить атрибуты: пробег, название, год, цена.
# В классе реализовать счетчик экземпляров,
# также определить магические методы str, eq(который будет сравнивать два экземпляра на
# основании названия и года. Далее реализовать
# метод для экземпляра класса, возвращающий цену в рублях и долларах. Метод класса для
# получения количества экземпляров данного класса,
# статический метод, принимающий марку автомобиля и возвращающий страну производства
# (здесь можно определить 3-4 страны и в остальных
# случаях возвращать любую строку), последнее это определить вычисляемый метод для
# получения пробега и для него определить setter и deleter.
# Далее реализовать дочерний класс какой-либо конкретоной марки автомобиля и в нем
# переопределить наследуемый статический метод.

class Car:
    count = 0

    def __init__(self, mileage, name, year, cost):
        Car.count += 1
        self.mileage = mileage
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}\n{self.year}\n{self.mileage}\n{self.cost}"

    def __eq__(self, other):
        return self.name == other.name and self.year == other.year

    def convert(self):
        return f"Cost in EURO = {self.cost}\n" \
                f"Cost in RUB = {self.cost * 68.73}\n" \
                f"Cost in $ = {self.cost * 1.06}"

    @classmethod
    def counter(cls):
        return Car.count

    @staticmethod
    def cars(Car):
        marks = {"Germany": ("Porsche", "MB", "BMW", "Audi"),
                 "Russia": ("Lada", "Kamaz", "UAZ", "GAZ"),
                 "Italy": ("Ferrari", "Lamborghini"),
                 "Japan": ("Honda", "Nissan")}
        result = None
        for k, v in marks.items():
            if Car.name in v:
                result = k
        return result

    @property
    def count_mileage(self):
        return self.mileage

    @count_mileage.setter
    def count_mileage(self, mileage):
        self.mileage = mileage
        return self.mileage

    @count_mileage.deleter
    def count_mileage(self):
        self.mileage = None
        return self.mileage



class CarHonda(Car):
    def __init__(self, mileage, name, year, cost):
        Car.__init__(self, mileage, name, year, cost)

    def convert(self):
        return f"Cost in Japan Iena = {self.cost * 0.0069}\n" \
               f"Cost in RUB = {self.cost * 0.47}\n" \
               f"Cost in $ = {self.cost * 0.0073}"

    def cars(self):
        return "Japan"
