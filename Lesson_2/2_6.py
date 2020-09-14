n = 1
products = []
product = ()
product_param = {"name": "1", "price": 0, "amount": 0, "units": "2"}
product_analytic = {"name": [], "price": [], "amount": [], "units": []}

k = int(input('Сколько продуктов вы планируете добавить? '))
for i in range(1, k+1):
    print(f'Пожалуйста, введите данные о продукте № {i}: ')
    product_param["name"] = input('Имя: ')
    product_param["price"] = int(input('Стоимость: '))
    product_param["amount"] = int(input('Кол-во: '))
    product_param["units"] = input('Ед.: ')

    product_analytic["name"].append(product_param["name"])
    product_analytic["price"].append(product_param["price"])
    product_analytic["amount"].append(product_param["amount"])
    product_analytic["units"].append(product_param["units"])

    product = (n, product_param.copy())
    products.append(product)
    n += 1

print('Итоговый список')
for el in products:
    print(el)

print('Проведем небольшую аналитику внесенных вами данных: ')
for key,el in product_analytic.items():
    print(f'{key}: {list(set(el))}')
    
