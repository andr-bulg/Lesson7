"""
Напишите программу, которая создаст дерево директорий,
изображенное на рисунке (см. picture.png). Выведите на экран только директории,
только файлы и файлы и директории, расположенные в директории Test.
"""
import os
dir_name = 'test_dir_dz/Test/'

# Создание конечной директории вместе с промежуточными рекурсивной функцией os.makedirs
# exist_ok=True - игнорирует ситуацию, когда конечная директория уже существует
os.makedirs(dir_name + 'A/A1/', exist_ok=True)
os.makedirs(dir_name + 'A/A2/', exist_ok=True)
os.makedirs(dir_name + 'B\\', exist_ok=True)
os.makedirs(dir_name + 'C\\', exist_ok=True)

# Создание файлов в указанных директориях (папках)
f = open(dir_name + 'A/A1/Test1.txt', 'w')
f.close()
f = open(dir_name + 'A/A2/Test2.txt', 'w')
f.close()
f = open(dir_name + 'B\\Test3.txt', 'w')
f.close()
f = open(dir_name + 'Test4.txt', 'w')
f.close()

print('Вывод на печать всех директорий: ')
# roots - путь к папке; dirs - список, расположенных в ней подпапок;
# files - список, расположенных в ней файлов
for roots, dirs, files in os.walk(dir_name, topdown=True):
    # normpath(roots) - нормализует выводимый путь, убирая лишние символы, типа, /
    roots = os.path.normpath(roots)
    print(roots)

print('\nВывод на печать всех файлов: ')
for roots, dirs, files in os.walk(dir_name, topdown=True):
    for file in files:
        # os.path.join(path, *paths) - соединяет один или несколько компонент пути
        # с учётом особенностей ОС в один общий путь
        print(os.path.join(os.path.normpath(roots), file))

# Получение списка директорий и файлов по указанному пути
objs = os.listdir(dir_name)
print('\nФайлы и директории, расположенные в директории Test:')
for obj in objs:
    p = os.path.join(dir_name, obj)
    # Проверка, если путь является файлом
    if os.path.isfile(p):
        print(f'файл {obj}')
    # Проверка, если путь является директорией
    elif os.path.isdir(p):
        print(f'папка {obj}')

