"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def wage(working_out, rate, bonus):
    return working_out * rate + bonus


def run():
    working_out, rate, bonus = [int(arg) for arg in argv[1:]]
    print(f'Заработная плата составляет: {wage(working_out, rate, bonus)}$')


run()
