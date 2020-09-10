gain = int(input('Введите выручку: '))
cost = int(input('Введите издержку: '))
if gain > cost:
    print('Состояние: Прибыль (выручка больше издержек)')
    print(f'Рентабельность: {gain / cost :.2f}')
elif cost < gain:
    print('Состояние: Убыток (выручка меньше издержек)')
else:
    print('Состояние: Баланс (выручка равна издержкам)')
all_coops = int(input('Введите количество сотрудников: '))
print(f'Прибыль на сотрудника: {(gain - cost) / all_coops :.2f}')
