try:
    lines = 0
    chars = 0
    exist_file = open(input("Введите имя файла для подсчета строк/символов: "), "r")
    while True:
        line = exist_file.readline()
        if not line: break
        lines += 1
        chars += len(line)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    print(f'Всего в файле {lines} строк и {chars} символов (из них {lines} - "Enter")')
    exist_file.close()