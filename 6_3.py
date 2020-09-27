class Worker():
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self):
        def try_str(string):
            while True:
                if string.isalpha():
                    return string
                else:
                    print('Введены некорректные символы. Повторите ввод.')
                    string = input()

        self.name = try_str(input('Введите имя сотрудника: '))
        self.surname = try_str(input('Введите фамилию сотрудника: '))
        self.position = try_str(input('Введите должность сотрудника: '))
        while True:
            try:
                self._income["wage"] = float(input('Введите оклад сотрудника: '))
                self._income["bonus"] = float(input('Введите премию сотрудника: '))
                break
            except ValueError:
                print('Введены некорректные данные.')

class Position(Worker):
    full_name = ""
    total_income = 0
    def get_full_name(self):
        self.full_name = self.surname + " " + self.name
        print(f'Фамилия и имя сотрудника: {self.full_name}')

    def get_total_income(self):
        self.total_income = round(sum(self._income.values()), 4)
        print(f'Доход сотрудника: {self.total_income}')

worker_1 = Position()
worker_1.get_full_name()
worker_1.get_total_income()

