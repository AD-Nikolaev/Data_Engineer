try:
    data_dict = dict()
    current_file = open("Lesson_5\\text_6.txt", "r", encoding="utf-8")
    for line in current_file:
        data_list = line.split("\n")
        print(data_list)
        for el in data_list[:-1]:
            key_name = el.split()[0][:-1] if el.split()[0][:-1].isalpha else False
            num_list = []
            num = ''
            for char in el:
                if char.isdigit():
                    num = num + char
                else:
                    if num != '':
                        num_list.append(int(num))
                        num = ''
            if num != '':
                num_list.append(int(num))
            sum_for_key = sum(num_list)
            data_dict[key_name] = sum_for_key
    print(data_dict)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    current_file.close()