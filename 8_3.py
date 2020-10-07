class NumberOnly(Exception):
    def __init__(self, txt):
        self.txt = txt

my_list = []
while True:
    next_number = input('Для завершения работы введите "q". \nВведите следующее число (действительное или целое) для списка: ')
    if next_number == "q":
        break
    try:
        if  all((letter.isdigit() or letter == ".") and next_number.count(".") <= 1 and next_number != "." for letter in next_number):
            my_list.append(float(next_number))
        else:
            raise NumberOnly('Введено не число! Данный элемент не будет добавлен в список.')
    except NumberOnly as err:
        print(err)
print(my_list)
