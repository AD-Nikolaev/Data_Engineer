from random import randint
try:
    numbers_list = [randint(0, 10) for _ in range(10)]
    print(f"Список записанный в файл text_5.txt: {numbers_list}")
    new_file = open("text_5.txt", "w")
    for number in numbers_list:
        print(number, end=" ", file=new_file)
    new_file.close()
    with open("text_5.txt", "r", encoding="utf-8") as exist_file:
        data_list = exist_file.read().split()
        list_number = [int(num) for num in data_list]
        print("Сумма чисел из файла text_5.txt: ", sum(list_number))
    exist_file.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
