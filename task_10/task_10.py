"""Построить иерархию классов, удовлетворяющую следующим условиям (тематика иерархии на ваше усмотрение):
- Количество классов >= 5.
- Использовать наследование, в т.ч. множественное
- Для каждого класса определить минимум 3 магических метода (на ваш выбор)
- Создать экземпляры для каждого класса
-  Иерархия должна быть логичной и не противоречить принципам ООП. """



class Animal:
    def __init__(self, paws_count, name):
        self.paws_count = paws_count
        self.name = name


class Predator:
    def eating(self):
        return f"This animal eat meat"


class Carnivore:
    def eating(self):
        return f"This animal eat carnivore"


class Cat(Animal, Predator):
    def __init__(self, paws_count, name):
        Animal.__init__(self, paws_count, name)


class Dog(Animal, Predator):
    def __init__(self, paws_count, name):
        Animal.__init__(self, paws_count, name)


class Bear(Animal):
    def __init__(self, paws_count, name):
        Animal.__init__(self, paws_count, name)


class Home:
    def living(self):
        return f"This animal lives at home"


class Wild:
    def living(self):
        return f"This animal lives in wild world"


class Panda(Bear, Wild, Carnivore):
    def __init__(self, paws_count=4, name=None):
        Bear.__init__(self, paws_count, name)
    def __str__(self):
        return f"This panda have {self.paws_count} paws.{self.eating()}"
    def __repr__(self):
        return f"{self.living(), self.paws_count, self.eating()}"


class Wolf(Dog, Wild):
    def __init__(self, paws_count=4, name=None):
        Dog.__init__(self, paws_count, name)

    def __str__(self):
        return f"This dog have {self.paws_count} paws.{self.eating()}"

    def __repr__(self):
        return f"{self.living(), self.paws_count, self.eating()}"


class Boxer(Dog, Home):
    def __init__(self, paws_count=4, name=None):
        Dog.__init__(self, paws_count, name)

    def __str__(self):
        return f"This dog have {self.paws_count} paws.{self.eating()}"

    def __repr__(self):
        return f"{self.living(), self.paws_count, self.eating()}"


class Sphinx(Cat, Home):
    def __init__(self, paws_count=4, name=None):
        Cat.__init__(self, paws_count, name)

    def __str__(self):
        return f"This cat have {self.paws_count} paws.{self.eating()}"

    def __repr__(self):
        return f"{self.living(), self.paws_count, self.eating()}"



panda_1 = Panda()
wolf_1 = Wolf()
sphinx_1 = Sphinx(name="Barsik")
dog_1 = Boxer(name="Stepan")
