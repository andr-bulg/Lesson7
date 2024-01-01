"""
Выведите на экран имена и размер всех непустых файлов созданного
в первой задаче дерева. Создайте директорию work/empty_files и переместите
в нее все пустые файлы, при этом для каждого перемещенного файла должно быть
выведено соответствующее сообщение, содержащее имя файла,
старый путь к файлу относительно корневой директории
и новый путь к файлу после перемещения.
"""

import os
dir_name = 'C:/test_30122023/Work/'

print("Имена и размер всех непустых файлов:")
for roots, dirs, files in os.walk(dir_name, topdown=True):
    for file in files:
        # os.path.join(path, *paths) - соединяет один или несколько компонент пути
        # в один общий путь
        p = os.path.join(os.path.normpath(roots), file)
        if os.path.getsize(p) > 0:
            print(f'{file}, {os.path.getsize(p)} bytes')


# Создание новой пустой папки
os.makedirs(dir_name + 'empty_files/', exist_ok=True)

# Перемещение пустых файлов в новую папку
for roots, dirs, files in os.walk(dir_name, topdown=True):
    for file in files:
        p = os.path.join(os.path.normpath(roots), file)
        if os.path.getsize(p) == 0:
            print(f'\nФайл {file} из директории {os.path.normpath(roots)}'
                  f' будет перемещён в {dir_name}empty_files')
            os.rename(p, dir_name + f'empty_files/{file}')

