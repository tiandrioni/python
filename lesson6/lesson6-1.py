"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep


class TrafficLight:
    __color = 'green'

    def __run(self, color, sleep_time):
        self.__color = color
        print(self.__color)
        sleep(sleep_time)

    def running(self, cycles_number=10):
        for _ in range(cycles_number):
            TrafficLight.__run(self, 'red', 7)
            TrafficLight.__run(self, 'yellow', 2)
            TrafficLight.__run(self, 'green', 10)


tl = TrafficLight()
tl.running()

