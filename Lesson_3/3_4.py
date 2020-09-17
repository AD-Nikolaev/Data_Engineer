def elevate_star(x, y):
    print(x**y)

def elevate_no_star(x, y):
    y *= -1
    x_help = x
    for el in range(y-1):
        x *= x_help
    print(1 / x)

try:
    x = float(input('Введите числo x: '))
    y = int(input('Введите числo y: '))    
except ValueError:
    print('Неверно введены данные!')
else:
    if y >= 0:
        print('y должен быть меньше 0!')
    else:
        elevate_star(x, y)
        elevate_no_star(x, y)

