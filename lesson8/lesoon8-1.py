"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
"""


class Date:
    def __init__(self, date_str: str):
        self.date_str = date_str

    @classmethod
    def conversion(cls, date_str: str):
        day, month, year = map(int, date_str.split('-'))
        return day, month, year

    @staticmethod
    def validation(day, month, year):
        month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month > 12 or month < 1:
            return False
        else:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0): # не високосный год
                month_days[1] = 28
            if day < 1 or day > month_days[month - 1]:
                return False
        return True


def run():
    print(Date.conversion('08-10-2021'))
    print(Date.validation(29, 2, 2023))
    date = Date.conversion('07-12-2019')
    print(Date.validation(*date))


run()
