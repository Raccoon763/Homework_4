"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

schet = 0
history = {}

def schet_pop(schet, popolnenie):
    schet += int(popolnenie)
    return schet

def sum_pok(schet, history, money):
    money = int(money)
    if money <= schet:
        schet -= money
        history[input('Введите название товара:')] = money
    else:
        print('Недостаточно средств')
    return schet, history

def sum_obsh(history):
    for i, p in history.items():
        print(f'{i} --> {p}')


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        schet = schet_pop(schet, input('Введите сумму, на которую хотите пополнить счёт:'))
        pass
    elif choice == '2':
        schet, history = sum_pok(schet, history, input('Введите сумму, которую планируете потратить на покупки:'))
        pass
    elif choice == '3':
        sum_obsh(history)
        pass
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')