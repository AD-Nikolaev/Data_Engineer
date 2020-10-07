class DevByZero(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0: raise DevByZero('Вы ввели делитель = 0!')
except ValueError:
    print('Вы ввели не целое число!')
except DevByZero as err:
    print(err)
else:
    print(f"a / b = : {a/b : 0.2f}")
