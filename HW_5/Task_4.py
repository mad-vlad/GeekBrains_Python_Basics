dictionary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

text_en = ''
with open('file_4.txt', 'r', encoding='UTF-8') as file_en:
    text_en = file_en.read()

text_ru = text_en
for en, ru in dictionary.items():
    text_ru = text_ru.replace(en, ru)

with open('file_4_new.txt', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(text_ru)

print(text_ru)