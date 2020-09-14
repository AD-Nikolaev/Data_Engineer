import random

n = int(input('Задайте кол-во чисел в списке: '))
print(f'Создаём список из {n} чисел: ')
num_list = []
start_list = []
for i in range(0,n):
    num_list.append(random.randint(1, 100))
    start_list.append(num_list[i])
    print(i)
    if (i+1) % 2 == 0:
        help_list = [num_list[i-1],num_list[i]]
        help_list.reverse()
        num_list[i-1] = help_list[0]
        num_list[i] = help_list[1]

print(f'Стартовый список: {start_list}')
print(f'Итоговый список: {num_list}')




