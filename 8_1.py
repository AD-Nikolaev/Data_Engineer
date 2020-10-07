class Date():

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, data):
        try:
            day, month, year = data.split(".")
            day = int(day)
            month = int(month)
            year = int(year)
        except (ValueError, AttributeError):
            print('Введены некорректные данные или нехватает аттрибутов! Ваши данные были обнулены.')
            day, month, year = "0.0.0".split(".")
        finally:
            return cls(day, month, year)

    @staticmethod
    def get_date(self):
        return f'{self.day} {self.month} {self.year}'

date_1 = Date.set_date("2.5.2000")
print(Date.get_date(date_1))
date_2 = Date.set_date(".5.2000")
print(Date.get_date(date_2))
date_3 = Date.set_date("2.5.20a00")
print(Date.get_date(date_3))
