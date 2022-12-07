"""Создать класс User, определить в нем конструктор с
    полями name, surname, age, country, gender, profession.
    Определить методы email, birth_year, которые будут возвращать
    год рождения и генерировать email на основании значений
    атрибутов. Затем определить еще 3 метода, каждый из которых
    будет создавать экземпляр класса User с определенной
    профессией( doctor, policeman, teacher)."""

from _datetime import datetime
from random import randint


NAME_MEN = ["Oliver", "Harry", "Jacob", "Charley", "Thomas", "George", "Oscar"]

NAME_WOMEN = ["Anna", "Maria", "Sophia", "Katherine", "Victoria", "Alexandra", "Eva", "Diana"]

SURNAMES = ["Evans", "Stone", "Roberts", "Mills", "Lewis", "Morgan", "Florence", "Campbell"]

COUNTRIES = ["Belarus", "Poland", "Australia", "Russia", "Germany", "USA"]



class User:
    def __init__(self, name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def email(self):
        return f"{self.name}.{self.surname}.{self.age}@gmail.com"

    def birth_year(self):
        return int(datetime.now().year - self.age)

    def repr(self):
        return f"{self.name} {self.surname}\nE-mail - <{self.email()}>\nBirth-year - {self.birth_year()}\n" \
               f"Age - {self.age}\nCountry - {self.country}\nGender - {self.gender}\n" \
               f"Profession - {self.profession}"


def generate_user(profession):
    gender_1 = randint(0, 1)
    if gender_1 == 0:
        return User(name=NAME_MEN[randint(0, len(NAME_MEN) - 1)], age=randint(20, 100),
                    country=COUNTRIES[randint(0, len(COUNTRIES) - 1)],
                    gender="Man", profession=profession, surname=SURNAMES[randint(0, len(SURNAMES) - 1)])
    else:
        return User(name=NAME_WOMEN[randint(0, len(NAME_WOMEN) - 1)], age=randint(20, 100),
                    country=COUNTRIES[randint(0, len(COUNTRIES) - 1)],
                    gender="Woman", profession=profession, surname=SURNAMES[randint(0, len(SURNAMES) - 1)])


def prof_teacher():
    return generate_user("Teacher")


def prof_doctor():
    return generate_user("Doctor")


def prof_policeman():
    return generate_user("Policeman")
