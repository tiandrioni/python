"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы
и т.д.
"""


class Matrix:
    def __init__(self, lines):
        self.lines = lines

    def check(self, other):
        if len(self.lines) == len(other.lines):
            for line in zip(self.lines, other.lines):
                if len(line[0]) == len(line[1]):
                    pass
                else:
                    return False
            return True
        else:
            return False

    def __str__(self):
        result_list = []
        for line in self.lines:
            result_list.append(' '.join(map(str, line)))
        return '\n'.join(result_list)

    def __add__(self, other):
        if Matrix.check(self, other):
            result = []
            for index in range(len(self.lines)):
                result.append([(lambda x, y: x + y)(x, y) for (x, y) in zip(self.lines[index], other.lines[index])])
            return Matrix(result)
        else:
            return 'Не совпадают размеры матриц'


def run():
    print('Матрица 1:')
    matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
    print(matrix1)
    print('Матрица 2:')
    matrix2 = Matrix([[1, 1, 1], [1, 1, 1]])
    print(matrix2)
    print('Матрица 3:')
    matrix3 = Matrix([[1, 1], [1, 1]])
    print('Матрица 4:')
    matrix4 = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(matrix3)
    print('Сумма матриц 1 и 2:')
    print(matrix1 + matrix2)
    print('Сумма матриц 1 и 3:')
    print(matrix1 + matrix3)
    print('Сумма матриц 1 и 4:')
    print(matrix1 + matrix4)


run()
