start_list = [7, 5, 3, 3, 2]
n = 0
k = 0
print(f'Начальный список: {start_list}')
user_number = int(input('Введите число для добавления в список: '))

if user_number in start_list:
    n = start_list.index(user_number)
    k = start_list.count(user_number)
    start_list.insert(n + k,user_number)  
else:
    for el in start_list:
        if el < user_number: 
            break
        else: 
            n += 1
    start_list.insert(n,user_number)

print(f'№ позиции нового числа в списке: {n + k}')
print(f'Конечный список: {start_list}')