from sys import argv

script_name, production, rate, award = argv
print(f'script_name: {script_name}')
user_args = argv[1:]

print(f'''В программу были введены следующие данные: 
Выработка (час): {production}
Ставка (час): {rate} 
Премия: {award}''')

print(f'\nЗарплата сотрудника: {int(production) * int(rate) + int(award)} у.е.\n')