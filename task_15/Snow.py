"""Создать класс Snow. Класс содержит целое число - количество снежинок.
Класс включает методы перегрузки арифметических операторов сложения, вычитания,
умножения и деления. Код этих методов должен выполнять увеличение или уменьшение
количества снежинок на число n или в n раз.
Класс также включает метод makeSnow(), который принимает сам объект и число
снежинок в ряду, а возвращает строку вида
"*****\n*****\n*****…",
где количество снежинок между '\n' равно переданному аргументу, а количество рядов
вычисляется, исходя из общего количества снежинок."""


class Snow:
    def __init__(self, number):
        self.number = number

    def __add__(self, n):
        return self.number + n

    def __sub__(self, n):
        return self.number - n

    def __mul__(self, n):
        return self.number * n

    def __divmod__(self, n):
        return self.number / n

    def makeSnow(self, number_of_snowflake_in_string: int):
        snow_split = ['*' for i in range(0, self.number)]
        snow_split = [snow_split[x:x + number_of_snowflake_in_string] for x in range(0, len(snow_split), number_of_snowflake_in_string)]
        print(*map("".join, snow_split), sep="\n")
