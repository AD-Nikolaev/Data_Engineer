from functools import reduce

start_list = [el for el in range(100, 1001)]

product = reduce((lambda x, y: x * y), start_list)

print(f'Произведение чисел от 100 до 1000 (БОЛЬШОЕ): {product}')