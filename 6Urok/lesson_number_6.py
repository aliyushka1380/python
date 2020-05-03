#1)	Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.  Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

import time
from  itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = (
        ("\033[91m {}" .format("Red"), 7),
        ("\033[93m {}" .format("Yellow"), 2),
        ("\033[92m {}" .format("Green"), 7),
        ("\033[93m {}" .format("Yellow"), 2)
        )

    def running(self):
        #c = 0
        for color, sec in cycle(self.__color):
            #if c > 10:
                #break
            print(color)
            time.sleep(sec)
            #c += 1

My_TrafficLight = TrafficLight()
My_TrafficLight.running()

#2)	Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def weight(self):
        return f"Масса асфальта: {self._length * self._width * 25 * 5}"
        # self.weight = _length * _width * 25 * 5

my_Road = Road(20, 5000)
print(my_Road.weight())

# 3)	Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.surname, self.name, self.position)

    def get_total_income(self):
        print(f"Доход на должности {self.position} составляет {self._income.get('wage') + self._income.get('bonus')}р.")

my_Position = Position("Иван", "Иванов", "Летчик", 50000, 20000)
my_Position.get_full_name()
my_Position.get_total_income()

# 4)	Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        self.direction = direction
        print('Машина повернула', self.direction)

    def show_speed(self):
        print('Текущая скорость автомобиля', self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {60 - self.speed}")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {40 - self.speed}")

class SportCar(Car):
    def show_color(self):
        print('Цвет автомобиля "', self.name, '" - ', self.color)

class PoliceCar(Car):
    def show_is_police(self):
        print('Это полицейская машина? ', self.is_police)


Town_Car = TownCar(80, 'Red', 'Городская машина', False)
Town_Car.show_speed()
Work_Car = WorkCar(80, 'Red', 'Рабочая машина', False)
Work_Car.show_speed()
Sport_Car = SportCar(80, 'Red', 'Спортивная машина', False)
Sport_Car.show_color()
Police_Car = PoliceCar(80, 'Red', 'Полицейская машина', True)
Police_Car.show_is_police()

#5)	Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
# метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print('Рисуем ручкой.')

class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом.')

class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером.')

pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()