import random

start_list = sorted([random.randint(0, 10) for el in range(10)])
end_list = []
print(f'Начальный список (отсортированный): {start_list}')

for el in start_list:
    if start_list.count(el) == 1:
        end_list.append(el)

print(f'Конечный список с уникальными элементами: {end_list}')