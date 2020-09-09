user_number = int(input('Введите целое положительное число: '))
number = user_number
max = 0
while number > 0:
    if number % 10 > max:
        max = number % 10
    number //= 10
print(f'Максимальная цифра в числе {user_number}: {max}')