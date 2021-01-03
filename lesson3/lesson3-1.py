"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(numerator, denominator):
    if denominator != 0:
        return numerator / denominator
    else:
        return 'Ошибка: деление на ноль.'


def run():
    numerator = int(input('Введите числитель: '))
    denominator = int(input('Введите знаменатель: '))
    print(f'{numerator} / {denominator} = {division(numerator, denominator)}')


run()
