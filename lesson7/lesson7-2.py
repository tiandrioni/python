"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов
проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Garment(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def consumption(self):
        pass


class Coat(Garment):
    def __init__(self, size):
        self.name = 'coat'
        self.size = size

    @property
    def consumption(self):
        return self.size / 6.5 + 0.5


class Suit(Garment):
    def __init__(self, height):
        self.name = 'suit'
        self.height = height

    @property
    def consumption(self):
        return 2 * self.height + 0.3


def run():
    coat = Coat(48)
    suit = Suit(1.70)
    print(coat.consumption)
    print(suit.consumption)


run()
