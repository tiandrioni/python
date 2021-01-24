"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def run():
    dict_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    with open('f4-in.txt') as f_in, open('f4-out.txt', 'w') as f_out:
        line = f_in.readline()
        while line:
            word = line.split(' — ')[0]
            line = line.replace(word, dict_trans[word])
            f_out.write(line)
            line = f_in.readline()


run()
