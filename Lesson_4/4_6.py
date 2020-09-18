from sys import argv
from random import randint

def iterator(iter_number):
    from itertools import count
    end = user_number + randint(5, 15)
    for el in count(iter_number):
        if el > end:
            print(f'Произведено чисел: {end - iter_number + 1}')
            print(f'Получен список чисел: {iter_list}')
            return iter_list
        else:
            iter_list.append(el)

def cycler(some_list):
    from itertools import cycle
    end = randint(15, 25)
    iter = cycle(some_list)
    for _ in range(end):
        print(next(iter), end=" ")
    print(f'\nКол-во выведенных элементов: {end}')


iter_list = []
script_name, user_number = argv
print(f'script_name: {script_name}')
user_number = int(user_number)
print(f'Вы ввели: {user_number}')
iter_list = iterator(user_number)
print('Выведем некоторое случайное количество раз полученные элементы списка с возможным повторением.')
cycler(iter_list)