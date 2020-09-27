import random

class Car():
    speed = 0
    colors = ["red", "green", "blue", "white", "black", "yellow", "red", "grey"]
    color = ""
    name = ""
    ct = ""
    is_police = False
    speed_up = 0
    speed_down = 0
    in_danger = False
    crash = False

    def __init__(self):
        self.color = self.colors[random.randint(0, 7)]
        def try_str(string):
            while True:
                if string.isalpha():
                    return string
                else:
                    print('Введены некорректные символы. Повторите ввод.')
                    string = input()
        self.name = try_str(input('Введите название машины: '))

    def info(self):
        print(f'Тип машины: {self.ct} \nНазвание: {self.name}; \nЦвет: {self.color}; \nСкорость: {self.speed}; \nУскорение: {self.speed_up}; \nСкорость торможения: {self.speed_down}; \nПолицейская: {self.is_police}.\n')

    def go(self, car_type):
        if car_type == "1" and self.speed == 0 and random.randint(1,2) == 1:
            print('А твоя машина не так проста ;) \nНачальная скорость увеличена на 50!')
            self.speed = 50
        else:
            self.speed += self.speed_up
        self.show_speed()

    def stop(self):
        if self.speed - self.speed_down <= 0:
            self.speed = 0
            print('Вы остановились. Не пробуйте опускать скорость дальше, не выйдет.')
        else:
            self.speed -= self.speed_down
        self.show_speed()

    def turn(self, direction):
        if direction == "a":
            print('Поворачиваем налево.')
        elif direction == "d":
            print('Поворачиваем направо.')

    def show_speed(self):
        print(f'Ваша текущая скорость: {self.speed}')

class WorkCar(Car):
    speed_up = 5
    speed_down = 10

    def __init__(self):
        super().__init__()

    def show_speed(self):
        if self.speed > 40 and self.speed <= 50:
            print(f'Вы набрали уже достаточно высокую скорость, притормозите. Скорость: {self.speed}')
        elif self.speed > 50 and self.speed <= 55:
            print(f'Вы набрали слишком высокую скорость. Сбросьте её или вас остановит полицейская машина! Скорость: {self.speed}')
        elif self.speed > 55:
            self.in_danger = True
        else:
            print(f'Ваша текущая скорость: {self.speed}')


class TownCar(Car):
    speed_up = 10
    speed_down = 20

    def __init__(self):
        super().__init__()

    def show_speed(self):
        if self.speed > 60 and self.speed <= 80:
            print(f'Вы набрали уже достаточно высокую скорость, притормозите. Скорость: {self.speed}')
        elif self.speed > 80 and self.speed <= 80:
            print(f'Вы набрали слишком высокую скорость. Сбросьте её или вас остановит полицейская машина! Скорость: {self.speed}')
        elif self.speed > 90:
            self.in_danger = True
        else:
            print(f'Ваша текущая скорость: {self.speed}')

class SportCar(Car):
    speed_up = 20
    speed_down = 40

    def __init__(self):
        super().__init__()

    def show_speed(self):
        if self.speed >= 120 and self.speed < 200:
            print(f'Стоит сбросить скорость, а то мало ли что... Скорость: {self.speed}')
        elif self.speed == 200:
            print(f'Ты вообще меня слушаешь? Уже {self.speed}!')
        elif self.speed > 200:
            self.crash = True
        else:
            print(f'Ваша текущая скорость: {self.speed}')

class PoliceCar(Car):
    is_police = True

car_type = input('Выберите тип машины (впишите указанное число): \n1 - Рабочая, \n2 - Городская, \n3 - Спортивная, \n4 - Полицейская.\n')
while True:
    if car_type == "1":
        Car.ct = "Рабочая"
        user_car = WorkCar()
        break
    elif car_type == "2":
        Car.ct = "Городская"
        user_car = TownCar()
        break
    elif car_type == "3":
        Car.ct = "Спортивная"
        user_car = SportCar()
        break
    elif car_type == "4":
        print('Все полицейские машины сейчас заняты. \nВам будет выдана случайная машина. \nНаслаждайтесь рандомом =)')
        car_type = str(random.randint(1,3))
    else:
        print('Введены некорреткные данные! Повторите ввод.')
        break

print('Начнём наш симулятор как бы движения или бесполезной езды машинки.')
print('''Управление:
w - поднять скорость;
s - сбавить скорость;
a - повернуть налево;
d - повернуть направо;
i - информация о машине;
is - узнать свою текущую скорость;
q - наконец-то завершить работу программы.
''')

user_input = ""
rand_input = False
while True:
    if rand_input:
        print(f'Выбрана команда {user_input}!')
    else: user_input = input()
    if user_input == "q":
        break
    elif user_input == "w":
        user_car.go(car_type)
    elif user_input == "s":
        user_car.stop()
    elif user_input == "a" or user_input == "d":
        user_car.turn(user_input)
    elif user_input == "i":
        user_car.info()
    elif user_input == "is":
        user_car.show_speed()
    else:
        rand_input = True
        user_input = random.choice(["q", "w", "q", "s", "q", "a", "q", "d"])
        print('Команда не распознана, будет выполнено рандомное действие!')
    if user_car.in_danger:
        print('Ну вот вас и поймали...')
        break
    if user_car.crash:
        print('Упс, разбилась машинка...')
        break

print('Этот странный симулятор завершает свою работу...')