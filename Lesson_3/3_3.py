def max_two_of_three(a1, a2, a3):
    print(sum([a1, a2, a3]) - min(a1, a2, a3))
    
try:
    a = input('Введите 3 числа через пробел: ') 
    a1, a2, a3 = (int(el) for el in a.split())
    max_two_of_three(a1, a2, a3)
except ValueError:
    print('Неверно введены данные!')

'''Функция лямбда на замену функции max_two_of_three
print((lambda a1, a2, a3: sum([a1, a2, a3]) - min(a1, a2, a3))(a1, a2, a3))'''

