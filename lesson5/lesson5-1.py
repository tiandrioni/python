"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def run():
    with open('f1.txt', 'w') as f:
        text = input()
        while text:
            f.write(text + '\n')
            text = input()


run()