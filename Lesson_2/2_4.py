user_string = input('Введите несколько слов через пробел: ')

user_list = list(user_string.split())
for ind, el in enumerate(user_list):
    print(f'{ind}) {el[0:10]}')


