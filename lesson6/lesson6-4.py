"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, name, color, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        if speed == 0:
            self.__status = 'stands'
        else:
            self.__status = 'ride'

    def go(self, speed):
        if self.__status == 'stands':
            self.__status = 'ride'
            print(f'{self.name} поехал')
        else:
            print(f'{self.name} поменял скорость движения')
        self.speed = speed

    def stop(self):
        if self.__status == 'ride':
            self.__status = 'stands'
            print(f'{self.name} остановился')
        else:
            print(f'{self.name} уже стоит')

    def turn(self, direction):
        print(f'{self.name} повернул на {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def nitro(self):
        self.speed += 100
        Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, name, color, speed):
        Car.__init__(self, name, color, speed, True)
        self.__police_flashers = 'off'

    def check_police_flashers(self):
        if self.__police_flashers == 'on':
            print(f'Мигалки на {self.name} включены')
        else:
            print(f'Мигалки на {self.name} выключены')

    def on_police_flashers(self):
        self.__police_flashers = 'on'
        PoliceCar.check_police_flashers(self)

    def off_police_flashers(self):
        self.__police_flashers = 'off'
        PoliceCar.check_police_flashers(self)


def run():
    dodge = Car('Dodge', 'red')
    dodge.go(90)
    dodge.show_speed()
    dodge.go(40)
    dodge.show_speed()
    dodge.stop()
    police_car = PoliceCar('Ford', 'white-blue', 60)
    police_car.on_police_flashers()
    print(police_car.is_police)
    police_car.show_speed()
    town_car = TownCar('kia', 'black', 70)
    town_car.turn('право')
    town_car.show_speed()
    town_car.go(55)
    town_car.show_speed()
    ferrari = SportCar('ferrari', 'red', 150)
    ferrari.nitro()
    print(ferrari.name, ferrari.color, ferrari.speed)
    work_car = WorkCar('stiga', 'white',  30)
    work_car.show_speed()


run()
