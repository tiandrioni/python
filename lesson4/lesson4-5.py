"""
Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""


from functools import reduce


def multiply(arg1, arg2):
    return arg1 * arg2


def run():
    even = [el for el in range(100, 1001) if el % 2 == 0]
    print(f'Произведение равно: {reduce(multiply, even)}')


run()
