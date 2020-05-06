#1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# __str__() для вывода матрицы в привычном виде,
# __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
# проверка на одинак колич объектов, + одинак количество 'элементов внутри

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join(str(el).replace('[', '').replace(']', '').replace(',', ' ') for el in self.matrix)

    def __add__(self, other):
        result = ''
        if len(self.matrix) == len(other.matrix):
            for one_line, two_line in zip(self.matrix, other.matrix):
                sum_lines = (el_1 + el_2 for el_1, el_2 in zip(one_line, two_line))
                result += '  '.join([str(el) for el in sum_lines]) + "\n"
        else:
            return 'Проверьте количество элементов матрицы'
        return result

matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])
print(matrix_1)
print(matrix_1 + matrix_2)

#2)	Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.  Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class MyAbstractClothes(ABC):
    @abstractmethod
    def coat(self):
        pass
    @abstractmethod
    def suit(self, H):
        pass
    @abstractmethod
    def __add__(self, other):
        pass

class Clothes(MyAbstractClothes):
    @property
    def coat(self):
        V = 42
        coat_cost = round(V / 6.5 + 0.5)
        return coat_cost

    def suit(self, H):
        self.H = H
        suit_cost = round(2 * self.H + 0.3)
        return suit_cost

    def __add__(self, other):
        return Clothes(self.suit() + other.coat())

my_clothes = Clothes()
a = my_clothes.coat
print(a)
b = my_clothes.suit(170)
print(b)
print(a + b)

#3)	Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, section):
        self.section = section

    def __add__(self, other):
        return str(self.section + other.section)

    def __sub__(self, other):
        return str(self.section - other.section) if (self.section - other.section) > 0 else "Разность - отрицательное число"

    def __mul__(self, other):
        return str(self.section * other.section)

    def __truediv__(self, other):
        return round(self.section / other.section) if other.section != 0 else "Делить на ноль нельзя"

    def make_order(self, num):
        return '\n'.join(["*" * num for i in range(self.section // num)]) + '\n' + "*" * (self.section % num)

cell_1 = Cell(34)
cell_2 = Cell(14)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_2.make_order(3))