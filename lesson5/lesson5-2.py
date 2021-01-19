"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def count_lines(lines):
    return len(lines)


def count_words(line):
    return len(line.strip().split())


def run():
    with open('f2.txt') as f:
        lines = f.readlines()
        print(f'Количество строк в файле: {count_lines(lines)}')
        print('Количество слов в каждой из строк файла:')
        for line in lines:
            print(count_words(line))


run()
