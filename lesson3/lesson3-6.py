"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    return word.capitalize()


def my_capitalize(words):
    new_words = []
    for word in words.split():
        new_words.append(int_func(word))
    result = ' '.join(new_words)
    return result


def run():
    words = input('Введите слова в нижнем регистре через пробел:\n')
    print('Результат работы программы:')
    print(my_capitalize(words))


run()
