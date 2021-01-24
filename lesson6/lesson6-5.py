"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'pen')

    def draw(self):
        print('Отрисовка ручкой запущена.')


class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'pencil')

    def draw(self):
        print('Отрисовка карандашом запущена.')


class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'handle')

    def draw(self):
        print('Отрисовка маркером запущена.')


def run():
    pen = Pen()
    pencil = Pencil()
    handle = Handle()
    for obj in [pen, pencil, handle]:
        obj.draw()


run()
