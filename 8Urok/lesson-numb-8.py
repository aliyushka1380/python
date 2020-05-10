"""1)	Реализовать класс «Дата», функция-конструктор которого должна принимать дату
в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

class Date:

    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)

    @classmethod
    def str_date(cls, dd_mm_yyyy):
        date_list = []
        for el in dd_mm_yyyy.split('-'):
            date_list.append(el)
        date = int(date_list[0]), int(date_list[1]), int(date_list[2])
        print(cls, date)
        return date

    @staticmethod
    def valid_date(dd_mm_yyyy):
        dd, mm, yyyy = map(int, dd_mm_yyyy.split('-'))
        if (dd >= 1 and dd <= 31 and dd != 0) and (mm >= 1 and mm <= 12 and mm != 0) and yyyy >= 1000:
            return dd, mm, yyyy
        else:
            print('Дата должна быть в формате dd-mm-yyyy')

Date.str_date('04 - 12 - 1987')
print(Date.valid_date('04 - 12 - 1987'))

"""2)	Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
 вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать 
 эту ситуацию и не завершиться с ошибкой."""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

# a = input("Введите делимое: ")
# b = input("Введите делитель: ")

try:
    a = int(input("Введите делимое: "))
    b = int(input("Введите делитель: "))
    if b == 0:
        raise OwnError("На нуль делить нельзя!")
except OwnError as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    print(f"{a} / {b} = {round(a / b, 2)} \n")

"""3)	Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
и заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь
сам не остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается,
сформированный список с числами выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число)
и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

result = []
while True:
    input_s = input("Введите число (stop - для завершения): ")
    if input_s == "stop":
        print(f"Сформированный список = {result}")
        break
    try:
        if not input_s.lstrip("-").isdigit():
            raise OwnError('Неверный тип')
        result.append(int(input_s))
    except OwnError as err:
        print(f"Значение {input_s} не было внесено в список - неверный тип")

"""
4)	
5)	
6)	
"""

# склад
class All_Equipmen:
    equipment_list = []
    _division_list = ["Бухгалтерия", "Производственный блок", "Административный блок"]

    division_eq = {
        _division_list[0]: [],
        _division_list[1]: [],
        _division_list[2]: []

    }

    def add_equipment(self, name, model, price, num):
        self.name = name
        self.model = model
        self.price = price
        self.num = num
        self.equipment_list.append(({'name': name, 'model': model, 'price': price, 'num': num}))
        for ind, el in enumerate(self.equipment_list, 1):
            print(ind, el)
        # print('\n', self.equipment_list)

    def relocation(self, el_equipm):
        self.el_equipm = el_equipm
        division_add = self._division_list[int(input('В какое подразделение передать оборудование? Ввести цифру "Бухгалтерия": 1, "Производственный блок": 2, "Административный блок": 3 ')) - 1]
        self.division_eq[division_add].append(el_equipm)
        self.equipment_list.remove(el_equipm)
        # print(f' Оборудование на складе: {self.equipment_list}')
        # print(f' Оборудование в подразделениях: {self.division}')

    def analitic(self):
        print('Оборудование на складе (количество и состав): ')
        for ind, el in enumerate(self.equipment_list, 1):
            print(ind, el)
        print('Оборудование в подразделениях: ', self.division_eq)
        for ind, el in self.division_eq.items():
            print(f'Количество оборудования в подразделении: {ind} {len(el)}')

#Класс оргтехника
class Office_equipment():

    def __init__(self):
        self.name = None
        self.model = input(f'Введите модель ')
        self.price = input(f'Введите цену в числовом формате ')
        if not self.price.isdigit():
            self.price = input(f'Внимание! Введите цену в числовом формате ')
        self.num = input(f'Введите количество в числовом формате ')
        if not self.num.isdigit():
            self.num = input(f'Внимание! Введите количество в числовом формате ')

#Класс Printer
class Printer(Office_equipment):

    def __init__(self):
        self.name = 'Printer'
        print(f'Приём {self.name} на склад: ')
        super().__init__()
        self.name = 'Printer'
        self.type_printer = input(f'Введите тип (лазерный, струйный...) ')
        el_equipment = ({'name': self.name, 'model': self.model, 'price': int(self.price),
                                             'num': int(self.num), 'type_printer': self.type_printer})
        All_Equipmen.equipment_list.append(el_equipment)
        for ind, el in enumerate(All_Equipmen().equipment_list, 1):
            print(ind, el)

        is_relocation = input("Передать оборудование в подразделение? Да - 1. Нет - 0.\n -- ")
        if is_relocation == "1":
            All_Equipmen().relocation(el_equipment)


#Класс Scanner
class Scanner(Office_equipment):

    def __init__(self):
        self.name = 'Scanner'
        print(f'Приём {self.name} на склад: ')
        super().__init__()
        self.name = 'Scanner'
        self.type_sensor = input(f'Введите тип датчика (CCD, CIS...) ')
        el_equipment = ({'name': self.name, 'model': self.model, 'price': self.price,
                                             'num': self.num, 'type_sensor': self.type_sensor})
        All_Equipmen.equipment_list.append(el_equipment)
        for ind, el in enumerate(All_Equipmen().equipment_list, 1):
            print(ind, el)

        is_relocation = input("Передать оборудование в подразделение? Да - 1. Нет - 0.\n -- ")
        if is_relocation == "1":
            All_Equipmen().relocation(el_equipment)

#Класс Xerox
class Xerox(Office_equipment):

    def __init__(self):
        self.name = 'Xerox'
        print(f'Приём {self.name} на склад: ')
        super().__init__()
        self.name = 'Xerox'
        self.availability_WiFi = input(f'Наличие Wi-Fi (Да, Нет) ')
        el_equipment = ({'name': self.name, 'model': self.model, 'price': self.price,
                                             'num': self.num, 'availability_WiFi': self.availability_WiFi})
        All_Equipmen.equipment_list.append(el_equipment)
        for ind, el in enumerate(All_Equipmen().equipment_list, 1):
            print(ind, el)

        is_relocation = input("Передать оборудование в подразделение? Да - 1. Нет - 0.\n -- ")
        if is_relocation == "1":
            All_Equipmen().relocation(el_equipment)


printers = Printer()
scanners = Scanner()
xeroxs = Xerox()
eq = All_Equipmen()
eq.analitic()

"""7)	Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата."""

class Complex:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.x * other.y + (self.y * other.x)} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


number_1 = Complex(2, -5)
number_2 = Complex(3, 4)
print(number_1)
print(number_2)
print(number_1 + number_2)
print(number_1 * number_2)