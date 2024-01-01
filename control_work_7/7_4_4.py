"""
Удалите из дерева директорий, созданного в первой задаче, ветвь,
расположенную под директорией F2, а также все пустые директории,
выводя соответствующие сообщения на экран.
"""

import os
dir_name = 'C:/test_30122023/Work/'

# Удаление директории F21 со всем ее содержимым
print(f'Файл {os.path.basename(dir_name + "F2/F21/f211.txt")} был удалён!')
os.remove(dir_name + 'F2/F21/f211.txt')
print(f"Файл {os.path.basename(dir_name + 'F2/F21/f212.txt')} был удалён!")
os.remove(dir_name + 'F2/F21/f212.txt')
print(f"Директория {os.path.dirname(dir_name + 'F2/F21/f212.txt')} была удалена!")
os.rmdir(dir_name + 'F2/F21')

for root, dirs, files in os.walk(dir_name, topdown=False):
    if not files and not dirs:
        print(f"Пустая директория {os.path.normpath(root)} была удалена!")
        # Функция os.rmdir(path) не удалит директории, которые стали
        # пустыми в следствие удаления дочерних директорий.
        # Для рекурсивного удаления родительских директорий
        # нужно использовать функцию os.removedirs(path).
        os.rmdir(root)

