"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию


year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')

МОЯ ОРИГИНАЛЬНАЯ ПРОГРАММА:

question = int(input('Введите год рождения А. С. Пушкина:'))
while question != 1799:
    question = int(input('Неверно, следующая попытка:'))
question_1 = float(input('Введите день рождения А. С. Пушкина:'))
while question != 25.05:
    question = float(input('Неверно, следующая попытка:'))
print('Верно')
"""
def year(x):
    while x != 1799:
        x = int(input('Неверно, следующая попытка:'))
def day(y):
    while y != 25.05:
        y = float(input('Неверно, следующая попытка:'))
    print('Верно')


year(input('Введите год рождения А. С. Пушкина:'))
day(input('Введите день рождения А. С. Пушкина:'))
