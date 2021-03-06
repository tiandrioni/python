"""
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


from random import randint


def run():
    start = [randint(0, 100) for _ in range(randint(5, 15))]
    print(f'Исходный список:\n {start}')
    finish = [start[index] for index in range(1, len(start)) if start[index] > start[index-1] ]
    print(f'Конечный список:\n {finish}')


run()

