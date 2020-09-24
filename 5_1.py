try:
    new_file = open(input("Введите имя файла (если файл уже уществует, то он будет дописан): "), "a")
    while True:
        line = new_file.write(input())
        if not line: break
        line = new_file.write("\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    new_file.close()
