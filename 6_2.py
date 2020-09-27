class Road():
    _length = int()
    _width = int()

    def weight(self, length, width):
        Road._length = length
        Road._width = width
        result = Road._length * Road._width * 25 * 5 / 1000
        print(f'{Road._length}м * {Road._width}м * 25кг * 5см = {result}т')

road_1 = Road()
print("Введите параметры дороги.")
try:
    road_1.weight(int(input("Длина: ")), int(input("Ширина: ")))
except ValueError:
    print("Введены некорректные данные.")