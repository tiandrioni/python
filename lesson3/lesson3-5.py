"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def check_input(input_line):
    if '$' in input_line:
        return True
    else:
        return False


def run():
    print('Для завершения ввода наберите $ в конце строки и нажмите Enter.')
    numbers_sum = 0
    check = False
    while not check:
        input_str = input('Введите числа через пробел: ')
        check = check_input(input_str)
        if check:
            input_str = input_str[:-1]
        if input_str == '':
            continue
        else:
            input_list = list(map(int, input_str.split()))
            numbers_sum += sum(input_list)
    print(f'Сумма введенных Вами чисел: {numbers_sum}')


run()


