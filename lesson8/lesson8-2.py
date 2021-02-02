"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class DivisionByZeroError(Exception):
    def __init__(self, text):
        self.text = text


def run():
    try:
        numerator = int(input('Введите числитель: '))
        denominator = int(input('Введите знаменатель: '))
        if denominator == 0:
            raise DivisionByZeroError('Деление на ноль!')
        result = numerator / denominator
    except ValueError:
        print('Вы ввели не число')
    except DivisionByZeroError as err:
        print(err)
    else:
        print(f'{numerator}/{denominator} = {numerator/denominator}')


run()
