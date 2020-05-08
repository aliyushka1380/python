"""
4)	Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
5)	Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
6)	Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""

# проверка типа оборудования
class EquipmentType(Exception):
    def __init__(self, message):
        self.message = message

# проверка артикула
class ArticleNumber(Exception):
    def __init__(self, message):
        self.message = message

# склад
class All_Equipmen:

    __equipment_list = {
        'printer': [],
        'xerox': [],
        'scanner': []
    }

    #учет техники
    __set_equipment = {

    }

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(All_Equipmen, cls).__new__(cls)
        return cls.instance

    #добавляем на склад
    def add_equipment(self, equip_type: str, equipment: dict):
        try:
            if not self.__equipment_list.get(equip_type):
                raise EquipmentType(f'Оборудование {equip_type} не учтено')

            self.__equipment_list[equip_type].append(equipment)
        except EquipmentType as error:
            print(error.message)

    #закрепляем за отделом
    def assign_equipment_to_structure(self, structure: str, equip_type: str, equipment_article_number: str):
        try:
            if not self.__equipment_list.get(equip_type):
                raise EquipmentType(f'Оборудование {equip_type} не учтено')

            if not self.__valid_article(equipment_article_number, equip_type):
                raise ArticleNumber(f'Артикул {equipment_article_number} не найден в {equip_type}')

            self.__set_equipment[structure][equip_type].append(equipment_article_number)

        except EquipmentType as error:
            print(error.message)
        except ArticleNumber as article_error:
            print(article_error.message)

    def __valid_article(self, equipment_article_number:str, equip_type:str):
        for item in self.__equipment_list[equip_type]:
            if item['article'] == equipment_article_number:
                return True
            else:
                return False

    # количество оргтехники
    def total_numb(self):
        result = {}
        for eq_type in self.__equipment_list:
            print(eq_type)
        return result

    # оставшаяся техника
    def remains_numb(self):
        full_numb = self.total_numb()
        assigned_numb = self.given_numb()
        result = {}
        for key, value in full_numb:
            result[key] = value - assigned_numb[key]

        return result

    # техника в подразделениях
    def given_numb(self):
        result = {}
        for structure, equipment in self.__set_equipment:
            for eq_type, eq_article_list in equipment:
                result[eq_type] += len(eq_article_list) if result.get(eq_type) is not None else len(eq_article_list)
        return result


class EquipmentInOffice:
    name: str
    article: str
    eq_type: str

    def add_item(self, **kwargs):
        self.__dict__.update(kwargs)


class Xerox(EquipmentInOffice):
    eq_type = 'xerox'
    is_color: bool


class NumericArticlePrinter(Exception):
    def __init__(self, message):
        self.message = message


class Printer(EquipmentInOffice):
    is_color: bool
    article: int
    eq_type = 'printer'

    def add_item(self, **kwargs):
        try:
            if not kwargs['article'].isdigit():
                raise NumericArticlePrinter('Артикул - число!')
            kwargs['article'] = int(kwargs['article'])
        except NumericArticlePrinter as error:
            print(error)


class Scanner(EquipmentInOffice):
    dpi: int
    eq_type = 'scanner'


Printer().add_item(
    name='Epson',
    is_color=True,
    article='112233'
)

All_Equipmen().add_equipment(Printer.eq_type, Printer.__dict__)

Scanner().add_item(
    name="Hp",
    dpi=12321,
    article='h021'
)

All_Equipmen().add_equipment(Scanner.eq_type, Scanner.__dict__)

Xerox().add_item(
    name='Samsung',
    is_color=False,
    article='xe214'
)

All_Equipmen().add_equipment(Xerox.eq_type, Scanner.__dict__)

All_Equipmen().total_numb()
All_Equipmen().given_numb()
All_Equipmen().remains_numb()