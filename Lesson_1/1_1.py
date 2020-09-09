print('Давайте проведём маленькую проверку.')
user_answer = int(input('Введите любое целое число: '))
print(f'Вы ввели: {user_answer}; тип: {type(user_answer)}.')
user_answer = input('Теперь введите слово "Привет" ')
print(f'Вы ввели: {user_answer}; тип: {type(user_answer)}.')
a = int(input('Теперь проверим операции. Введите а: '))
b = int(input('Введите b: '))
print(
f'''1) a + b = {a + b}
2) a - b = {a - b}
3) a * b = {a * b}
4) a / b = {a / b:.2f}
5) a ** 2 = {a ** 2}
6) a % b = {a % b}
7) a // b = {a // b}
''')