"""Напишите программу с классом Car. Создайте конструктор (__init__)
    класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
    Напишите три метода для этого класса. Первый — запуск автомобиля, при его вызове
    выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит
    сообщение «Автомобиль заглушен». Третий - магический метод str
    для вывода атрибутов экземпляра в виде строки."""

class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        return f"Автомобиль заведен"

    def stop(self):
        return f"Автомобиль заглушен"

    def __str__(self):
        return f"color - {self.color}, " \
               f"type - {self.type}, " \
               f"year - {self.year}"
