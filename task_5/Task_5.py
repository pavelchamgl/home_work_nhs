
"""1. Дана строка, состоящая из слов, вернуть длину кратчайшего слова(слов)."""

def get_shotest (array: str) -> int:
    return len(min(array.split(), key=len))



"""2. Проверьте, если строка имеет одинаковое количество " х " и "о".
Метод должен возвращать логическое True/False если количесвто разное. Без учета регистра.
Примеры строк:
XO("ooxx") => true  x==o
XO("xooxx") => false x!=0 o!=0
XO("ooxXm") => true x==o
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true 
XO("zzoo") => false"""

def get_equal(array: str) -> bool:
    return array.lower().count("x") == array.lower().count("o")



"""3. Реализовать функцию, которая проверяет, является слово изограммой или нет.
Изограмма - слово,  в котором нет повторяющихся символов."""

def is_isogram(array: str) -> bool:
        return len(array.lower()) == len(set(array.lower()))



"""4. [1,2,'a','b',3] == [1, 2, 3]    -> 1 + 4 + 9 = 14"""

def filter_list(lst: list) -> list:
    list_nums = [num for num in lst if type(num) == int]
    return list_nums

def sum_list(lst: list) ->int:
    result = sum(map(lambda a: pow(a, 2), lst))
    return result
