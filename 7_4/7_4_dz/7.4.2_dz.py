"""
Напишите программу, которая отредактирует файл Test4.txt
из предыдущего задания, записав в него некоторый текст,
а затем обрежет полученный файл до 10% от его размера.
Выведите содержимое полученного файла на экран.
"""
import os

dir_name = 'test_dir_dz/Test/Test4.txt'

# Создание файла Test4.txt и запись в него строки '1234567890'
with open(dir_name, 'w') as f:
    f.write('1234567890')

# Определение размера файла Test4.txt в байтах
size = os.path.getsize(dir_name)
# os.path.basename(dir_name) - возвращает последний компонент пути, т.е. имя файла
print(f'Размер файла {os.path.basename(dir_name)} составляет {size} bytes')

# Обрезание файла по указанному пути до указанной длины (в байтах))
os.truncate(dir_name, size//10)
size = os.path.getsize(dir_name)
print(f'Размер файла {os.path.basename(dir_name)} составляет {size} bytes')

# Чтение и вывод данных на печать из файла Test4.txt
print(f'Содержимое файла {os.path.basename(dir_name)}:')
with open(dir_name, 'r') as f:
    print(f.read())

