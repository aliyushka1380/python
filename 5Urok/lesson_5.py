#1)	Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#2)	Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

out_f = open("text_1_2.txt", "x+")
str_list = []
while True:
    text = input('Введите данные:')
    str_list.append(text)
    out_f.writelines(text + '\n')
    if not text:
        break

out_f.seek(0)
count = 0
for line in out_f:
    print(f"Количество слов в {count + 1} строке - {line.count(' ')}")
    count += 1
print(f"Количество строк - {count}")

out_f.close()

#3)	Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

import codecs
salary = codecs.open("text_3.txt", "r+", "utf-8")
my_list = []
lines = [my_list.append(line.strip().split(" ")[0]) for line in salary if float(line.strip().split(" ")[1]) <= 20000.0]
print("Кто из сотрудников имеет оклад менее 20 тыс.: " + '\n' + '\n'.join(my_list))
salary.seek(0)
count = 0
salary_sum = 0
for line in salary:
    count += 1
    salary_sum += float(line.strip().split(" ")[1])
print(f"Cредняя величина дохода сотрудников - {round(salary_sum / count, 2)}")

salary.close()

#4)	Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import codecs

out_f = codecs.open("text_4.txt", "r", "utf-8")
new_dict = []
my_dict = {
    "One": "Один",
    "Two": "Два",
    "Three": "Три",
    "Four": "Четыре",
}

lines = [new_dict.append(my_dict.get(line.strip().split(" - ")[0]) + " - " + line.strip().split(" - ")[1]) for line in out_f]
print('\n'.join(new_dict))

with codecs.open("text_44.txt", 'w', "utf-8") as file:
    file.write('\n'.join(new_dict))

out_f.close()

#5)	Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

out_f = open("text_5.txt", "x+")

numbers = out_f.writelines(input("Введите числа, разделенные пробелами: "))
out_f.seek(0)
sum = 0
for line in out_f:
    for el in line.split():
        sum += int(el)
print(sum)

out_f.close()

#6)	Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы
# для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика:   100(л)   50(пр)   20(лаб). Физика:   30(л)   —   10(лаб) Физкультура:   —   30(пр)   —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import codecs

out_f = codecs.open("text_6.txt", "r+", "utf-8")

out_f.seek(0)
my_dict = {}
for line in out_f:
    sum = 0
    for el in line.replace(' ', '(').split('('):
        if el.isdigit() == True:
            sum += int(el)
    #print(f"{line.replace(' ', '(').split('(')[0].replace(':', '')} {sum}")
    my_dict[line.replace(' ', '(').split('(')[0].replace(':', '')] = sum

print(my_dict)

out_f.close()

#7)	Создать вручную и заполнить несколькими строками текстовый файл, в котором
# каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1   ООО   10000   5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import codecs
import json

out_f = codecs.open("text_7.txt", "r+", "utf-8")

out_f.seek(0)
my_dict = {}
average_profit = 0
count = 0
for line in out_f:
    lines = line.strip().split(' ')
    profit = int(lines[2]) - int(lines[3])
    my_dict[lines[0]] = profit
    if profit > 0:
        average_profit += profit
        count += 1
ite = [my_dict, {'average_profit': int(average_profit / count)}]
print(ite)

with codecs.open("text_77.json", "w") as write_f:
    json.dump(ite, write_f)

out_f.close()