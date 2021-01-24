"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def lines_to_dict(lines):
    result = {}
    for line in lines:
        last_name, salary = line.split()
        result[last_name] = int(salary)
    return result


def stat(data, bound=20000):
    result = [key for key in data.keys() if data[key] < bound]
    return result


def average_salary(data):
    emp_num = len(data)
    return sum(data.values()) / emp_num


def run():
    with open('f3.txt') as f:
        lines = f.readlines()
        data = lines_to_dict(lines)
        special_list = stat(data)
        print(f'Средний заработок сотрудников: {average_salary(data)}')
        if len(special_list) > 0:
            print('У следуюжих сотрудников оклад меньше 20 тыс.:')
            print('\n'.join(special_list))
        else:
            print('У всех сотрудников оклад больше 20 тыс.')


run()

