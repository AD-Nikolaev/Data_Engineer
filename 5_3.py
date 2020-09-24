try:
    print('Сотрудники получившие более 20000 у.е.: ')
    average_income = 0.0
    lines = 0
    exist_file = open("text_3.txt", "r", encoding="utf-8")
    while True:
        line = exist_file.readline()[:-1]
        lines += 1
        if not line: break
        for word in line.split():
            if word.replace('.','',1).isnumeric():
                average_income += float(word)
                print(surname) if float(word) > 20000 else False
            else:
                surname = word
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    print(f'Средний доход сотрудников: {round(average_income / lines, 4)} у.е.')
    exist_file.close()
