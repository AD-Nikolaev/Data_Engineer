"""
Для перевода использовалась библиотека Translator из googletrans
Не забудьте установить pip install googletrans
"""
from googletrans import Translator
translator = Translator()
try:
    translate_file = open("text_4.txt", "r", encoding="utf-8")
    for line in translate_file:
        print(translator.translate(line, dest="ru").text)
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    translate_file.close()