"""
Напишите программу, генерирующую в заданной директории 26 текстовых файлов:
A.txt, B.txt, C.txt, ….., Z.txt, каждый из которых содержит
соответствующую букву английского алфавита.
* Вы можете внести в программу буквы алфавита вручную
  или воспользоваться атрибутом ascii_uppercase модуля string (string.ascii_uppercase).
"""
import string

file_name = 'C:\\test_29122023\\{}.txt'
for letter in string.ascii_uppercase:
    with open(file_name.format(letter), 'w') as f:
        f.write(f'{letter}\n')
        f.close()

print("Файлы успешно созданы!")

