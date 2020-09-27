class Statinery():
    title = input("Введите название: ")

    def draw(self):
        print("Запуск отрисовки...")

class Pen(Statinery):

    def draw(self):
        print("Выбран инструмент: Ручка.")

class Pencil(Statinery):

    def draw(self):
        print("Выбран инструмент: Карандаш.")

class Handle(Statinery):

    def draw(self):
        print("Выбран инструмент: Маркер.")

user_stat = Statinery()
user_stat.draw()

while True:
    tool = input("Для выбора инструмента введите: 1 - Ручка; 2 - Карандаш; 3 - Маркер.  ")
    if tool == "1":
        user_stat = Pen()
        user_stat.draw()
    elif tool == "2":
        user_stat = Pencil()
        user_stat.draw()
    elif tool == "2":
        user_stat = Handle()
        user_stat.draw()
    else:
        print("Задан некорректный параметр.")
        break