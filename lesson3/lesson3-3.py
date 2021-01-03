"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    return arg1 + arg2 + arg3 - min(arg1, arg2, arg3)


def run():
    args_str = input('Введите три числа через пробел: ').split()
    args = list(map(int, args_str))
    print(my_func(*args))


run()