month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
number_month = int(input('Введите номер месяца: '))

for i in month_dict:
    print(f'Время года: {i}') if number_month in month_dict.get(i) else False
        
        
