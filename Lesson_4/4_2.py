import random

start_list = [random.randint(0, 10) for el in range(10)]

# start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Исходный список: {start_list}')
print(f'Элементы, которые больше предыдущих: ', end="")
i = 1
for el in start_list[1:]:
    if start_list[i] > start_list[i-1]:
        print(el, end="; ")
    i += 1