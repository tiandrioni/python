class ComplexNum:
    def __init__(self, real, im):
        self.real = real
        self.im = im

    def __mul__(self, other):
        result_real = self.real * other.real - self.im * other.im
        result_im = self.real * other.im + other.real * self.im
        return ComplexNum(result_real, result_im)

    def __add__(self, other):
        result_real = self.real + other.real
        result_im = self.im + other.im
        return ComplexNum(result_real, result_im)

    def __str__(self):
        return f'{self.real} + {self.im}j'


def run():
    num1 = ComplexNum(1, 1)
    num2 = ComplexNum(2, 2)
    print(num1 + num2)
    print(num1 * num2)


run()

