"""1. Написать функцию, которая будет конвертировать любую переданную ей строку в CamelCase.
    "the-stealth-warrior" -> "theStealthWarrior"
    "The_Stealth_Warrior" -> "TheStealthWarrior"""

import re

def camel_case(array: str) -> str:
    result = re.split("-|_| |!|:|;|,", array)
    return result[0] + "".join([word.capitalize() for word in result[1:]])



"""2. Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром. 
    11 -> 22 
    188 -> 191 
    191 -> 202 
    2541 -> 2552"""

def next_polindrom(num: int) -> int:
    num += 1
    while str(num) != str(num)[::-1]:
        num = int(num + 1)
    return num



"""3. Передана строка, у которой внутри каждого слова спрятана цифра. Отсортируйте эти слова по значению спрятанной цифры.
    "is2 Thi1s T4est 3a"  ->  "Thi1s is2 3a T4est" """

def sorted_digit(strng: str) -> str:
    result = {}
    for word in strng.split():
        for symbol in word:
            if symbol.isdigit():
                result[symbol] = word
    sorted_dct = dict(sorted(result.items()))
    return " ".join(map(str, sorted_dct.values()))
