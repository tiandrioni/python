"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


def read():
    base = {}
    with open('f7.txt') as f:
        lines = f.readlines()
        for line in lines:
            firm, form, proceeds, costs = line.split()
            base[firm] = int(proceeds) - int(costs)
        profit_list = [value for value in base.values() if value >= 0]
        ev_profit = sum(profit_list) / len(profit_list)
        result = [base, {'average_profit': ev_profit}]
    return result


def write(data):
    with open('7.json', 'w') as f:
        f.write(json.dumps(data))


def run():
    statistic = read()
    write(statistic)


run()
