"""
Выведите на экран сначала все файлы, а затем все директории,
расположенные в корневой директории созданного в предыдущей задаче дерева.
"""

import os
dir_name = 'C:/test_30122023/Work/'

# получаем список директорий и файлов, находящихся в dir_name
objs = os.listdir(dir_name)

files = []
folders = []

for obj in objs:
    p = os.path.join(dir_name, obj)
    if os.path.isfile(p):
        files.append(obj)
    elif os.path.isdir(p):
        folders.append(obj)

if files:
    for el in files:
        print('Файл: {}'.format(el))

if folders:
    for el in folders:
        print(f'Директория: {el}')


