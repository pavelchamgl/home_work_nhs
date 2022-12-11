"""Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент
    при инициализации (отвечающий за добавку к выбираемому лимонаду).
    В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}»
    в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка»."""


class Soda:
    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        if bool(self.additive) == True:
            return f"Газировка и {self.additive}"
        else:
            return "Обычная газировка"


soda_strawberry = Soda(additive="Клубника")

print(soda_strawberry.show_my_drink())
