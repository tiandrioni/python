"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint


def write():
    with open('f5.txt', 'w') as f:
        nums = [randint(1, 100) for _ in range(randint(10, 25))]
        for num in nums:
            f.write(str(num) + ' ')


def read():
    with open('f5.txt') as f:
        nums_str = f.read().strip().split()
        nums = [int(num) for num in nums_str]
        print(f'Сумма чисел: {sum(nums)}')


def run():
    write()
    read()


run()

