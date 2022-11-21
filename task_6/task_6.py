"""1. Написать функцию, которая будет принимать целое положительное число
    и возвращать True, если это число простое, иначе - False. """

def is_prime(number: int) -> bool:
    return number > 1 and number % 2 != 0


"""2. На вход функции передается строка вида: "1 9 3 4 -5 " необходимо
    вернуть максимальное и минимальное число из этой последовательности."""

def max_min(strng: str) -> tuple:
    numbers = list(map(int, strng.split()))
    return max(numbers), min(numbers)



"""3. Написать функцию, принимающую строку вида: "The sunset sets at twelve o' clock."
    и возвращающую строку: "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
    где каждое число это порядковый номер буквы в алфавите.
    Например при передаче строки: "abc" должно вернуться "1 2 3". *Без учета регистра."""

def str_to_index(strng: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = []
    for literal in strng.lower():
        if literal in alphabet:
            result.append(alphabet.index(literal) + 1)
    return " ".join(map(str, result))
