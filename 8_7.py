class CompNumb():

    def __init__(self, cn):
        cn.replace(" ", "")
        if cn.find("+") != -1:
            help_list = cn.split("+")
            self.b = int(help_list[1][:-1])
            self.operation = "+"
        else:
            help_list = cn.split("-")
            self.b = int(help_list[1][:-1]) * -1
            self.operation = "-"
        self.a = int(help_list[0])

    def __str__(self):
        if self.operation == "+":
            return f"{self.a} {self.operation} {self.b}i"
        else:
            return f"{self.a} {self.operation} {self.b * -1}i"

    def __add__(self, other):
        if self.b + other.b >= 0:
            return f'cn_1 + cn_2 = {self.a + other.a} {self.operation} {self.b + other.b}i'
        else:
            return f'cn_1 + cn_2 = {self.a + other.a} {other.operation} {(self.b + other.b) * -1}i'

    def __mul__(self, other):
        if self.a * other.b + other.a * self.b >= 0:
            return f'cn_1 * cn_2 = {self.a * other.a - self.b * other.b} {self.operation} {self.a * other.b + other.a * self.b}i'
        else:
            return f'cn_1 * cn_2 = {self.a * other.a - self.b * other.b} {other.operation} {(self.a * other.b + other.a * self.b) * -1}i'

cn_1 = CompNumb("3 + 1i")
print(f"cn_1 = {cn_1}")
cn_2 = CompNumb("2 - 3i")
print(f"cn_2 = {cn_2}")

rez = cn_1 + cn_2
print(rez)
rez = cn_1 * cn_2
print(rez)