import json
try:
    open_f = open("text_7.txt", "r", encoding="utf-8")
    companys = dict()
    for line in open_f.readlines():
        a,b,c,d = line.split()
        companys[a] = int(c) - int(d)
    print(f"Данные полученные из текстового файла:\n {companys}")
    print(f"Средняя выручка: {round(sum(companys.values()) / len(companys), 4)}")
    average_profit = dict()
    average_profit["average_profit"] = round(sum(companys.values()) / len(companys), 4)
    company_list = [companys, average_profit]
    print(f"Данные для печати в json файл:\n {company_list}")    
    with open("text_71.json", "w", encoding="utf-8") as write_f:
        json.dump(company_list, write_f, sort_keys=False, indent=4, ensure_ascii=False)
    
    
    with open("text_77.json", "r", encoding="utf-8") as read_f:
        data = json.load(read_f)
    print(f"Содержимое файла text_77.json:\n {json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)}")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    open_f.close()
    write_f.close()

    