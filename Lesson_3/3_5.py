def summ(numbers, sum_last):
    numbers_list = [int(el) for el in numbers.split()]
    for el in numbers_list:
        sum_last += el
    return sum_last

sum_all = 0 # Общая сумма

while True:
    try:
        numbers = input('Введите числа для суммы через пробел: ')
        sum_last = 0 # Сумма последних введенных чисел
        sum_last = summ(numbers, sum_last)
        sum_all += sum_last    
        print(f'{sum_all}({sum_last}) - общая сумма (Сумма последних введенных чисел)')
        escape = input('Для продолжения нажмите Enter, для завершения - наберите "q" ')
        if escape == "q":
            print(f'\nИтого: {sum_all}')
            print('Завершение программы...')
            break
    except ValueError:
        print('\nНеверно введенные данные!\n')
