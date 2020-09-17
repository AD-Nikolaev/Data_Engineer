
'''Решение без конструкции  try except и без отлова ошибки ввода данных.
def div (d1, d2):
    if d2 == 0:
        print('Ошибка! Деление на 0!')
    else:
        return print(f'{d1 / d2 :.04f}')

d1, d2 = map(int, input('Введите 2 целых числа для деления, через пробел: ').split())
div(d1, d2)'''

# Деление 2-х чисел с отловом ошибок ввода и деления на 0
def div (d1, d2):
    try:
        return print(f'{d1 / d2 :.04f}')
    except ZeroDivisionError:
        print('Ошибка! Деление на 0!')
try:
    d1, d2 = map(int, input('Введите 2 целых числа для деления, через пробел: ').split())
    div(d1, d2)
except ValueError:
    print('Неверно введённые данные!')


