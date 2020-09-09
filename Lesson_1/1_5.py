gain = int(input('Введите выручку: '))
cost = int(input('Введите издержку: '))
if gain > cost:
    print('Прибыль')
    print(f'Рентабельность: {gain / cost :.2f}')
elif cost < gain:
    print('Убыток')
else:
    print('Баланс')
all_coops = int(input('Введите количество сотрудников: '))
print(f'Прибыль на сотрудника: {(gain - cost) / all_coops :.2f}')
