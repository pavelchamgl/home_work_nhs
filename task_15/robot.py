"""Создать класс Robot
Класс инициализируется начальными координатами – положением Робота на
плоскости, обе координаты заключены в пределах от 0 до 100.
Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W).
Выйти за границы плоскости Робот не может.
Метод move() принимает строку – последовательность команд перемещения робота,
каждая буква строки соответствует перемещению на единичный интервал в направлении,
указанном буквой. Метод возвращает список координат – конечное положение Робота
после перемещения"""


from random import randint


class Robot:
    def __init__(self):
        self.pos_x = randint(0, 100)
        self.pos_y = randint(0, 100)

    def move(self, array: str):
        array_split = list(map(int, array.split()))
        new_x = self.pos_x + array_split[2] - array_split[3]
        new_y = self.pos_y + array_split[0] - array_split[1]

        if new_x <= 100 and new_x > 0 and new_y <= 100 and new_y > 0:
            return [new_x, new_y]
        else:
            return "Write correct position X and Y"
