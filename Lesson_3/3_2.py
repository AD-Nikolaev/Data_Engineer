'''Проверок ввода данных в данной программе нет.'''
user_information = {"name": "", "surname": "", "birthday": "", "sity": "", "email": "", "phone": 0}
users = []
user = ()
n = 1

def user_add(users,n,user,user_information):
    try:
        print('Введите следующие данные: ')
        user_information["name"] = input('Имя: ')
        user_information["surname"] = input('Фамилию: ')
        user_information["birthday"] = input('День рождения (в формате dd.mm.yyyy): ') 
        user_information["sity"] = input('Город проживания: ')
        user_information["email"] = input('Email адрес: ')
        user_information["phone"] = int(input('номер телефона (к примеру, 74951234567): '))    
        user = (n, user_information.copy())
        users.append(user)
        print()
        return users
    except ValueError:
        print('Ошибка ввода данных!')
        return
    
        
def user_out(users,user,user_information,user_number):
    user_information = list(users[user_number-1])[1]
    for key, el in user_information.items():
        print(f'{key}: {el}')
    print()
    

while True:
    answer = input(f'''Для добавления {n}-го пользователя введите "y", 
для окончания программы - "q",
для вывода списка пользователей - "v": 
для вывода конкретного пользователя введите "vn", а затем его номер: ''')
    if answer == "y":
        user_add(users,n,user,user_information)
        n += 1
    elif answer == "v":
        for ind, el in users:
            print(f'{ind}) {el}')
    elif answer == "vn":
        user_number = int(input('Введите номер пользователя для вывода: '))
        user_out(users,user,user_information,user_number)
    elif answer == "q":
        break
    else:
        print('Команда не распознана.')
