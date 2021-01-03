"""
Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    result = 1
    for i in range(abs(y)):
        result = result / x
    return result


def run():
    x = float(input('Введите действительное положительное число: '))
    y = int(input('Введите целое отрицательное число: '))
    print(f'Возведение {x} в степень {y}:')
    print('-- через оператор **:', my_func1(x, y))
    print('-- с помощью цикла:', my_func2(x, y))


run()
