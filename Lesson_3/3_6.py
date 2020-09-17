def title_text(text):
    text_list = [el for el in text.split()]
    for el in text_list:
        print(el.title(), end=" ")
def only_lower_letters(text):
    return all(97 < ord(letter) < 122 or ord(letter) == 32 for letter in text)

text = input('Введите 1 или несколько слов через пробел: ')
if only_lower_letters(text):
    title_text(text)
else:
    print('Вы ввели не только английские буквы или не в нижнем регистре!')