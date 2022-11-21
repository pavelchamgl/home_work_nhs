import math
from random import randint

"""1. Функция находит наименьшее общее кратное для двух чисел."""

def nok(a: int,b: int) -> int:
    return (math.lcm(a, b))



"""2. Функция суммирует все целые числа от значения «start»
до величины «end» включительно."""

def sum_range(start: int, end: int) -> int:
    if start > end:
        start, end = end, start
    return sum(range(start, end + 1))



"""3. Написать программу, которая посчитает кол-во одинаковых элементов в списке.  
 Список будет заполняться рандомными целыми числами.  
 Рекомендую использовать несколько функций  
 (для заполнения списка целыми числами, для подсчета количества)"""

def random_list(start: int, end: int, count: int) -> list:
    random_list = []
    for _ in range(1, count + 1):
        random_list.append(randint(start, end))
    return random_list

def count_same(n: list) -> int:
    counetr = 0
    for num in set(n):
        if n.count(num) > 1:
            counetr += 1
    return counetr
