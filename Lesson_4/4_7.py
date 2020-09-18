def fact(n):
    a, b = 1, 2
    for el in range(n):
        yield a
        a, b = a * b, b + 1 

n = int(input('Факториал какого числа вы хотите получить: '))
fact_n = 1
fact_gen = fact(n)
for el in fact_gen:
    fact_n = el
print(f'Факториал числа {n}: {fact_n}')

