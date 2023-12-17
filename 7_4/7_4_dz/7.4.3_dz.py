"""
Напишите программу, которая выполнит следующие действия
над деревом директорий, созданным в первой задаче:
⦁	удалит файл Test2.txt, а затем директорию A2
⦁	переименует файл Test3.txt в Test2.txt
⦁	удалит директорию A со всем ее содержимым
⦁	переместит файл Test4.txt в директорию C
⦁	удалит корневую директорию Test
"""

import os

dir_name = 'test_dir_dz/'

# Удаление файла Test2.txt, а затем директории A2
os.remove(dir_name + 'Test/A/A2/Test2.txt')
os.rmdir(dir_name + 'Test/A/A2/')

# Переименование файла Test3.txt из папки B в Test2.txt
os.rename(dir_name + 'Test\\B\\Test3.txt', dir_name + 'Test/B/Test2.txt')

# Удаление директории A со всем ее содержимым
os.remove(dir_name + 'Test/A/A1/Test1.txt')
os.rmdir(dir_name + 'Test/A/A1')
os.rmdir(dir_name + 'Test/A/')

# Перемещение файла Test4.txt в директорию C
os.rename(dir_name + 'Test/Test4.txt', dir_name + 'Test\\C\\Test4.txt')

# Удаление корневой директории Test
os.remove(dir_name + 'Test/B/Test2.txt')
os.remove(dir_name + 'Test\\C\\Test4.txt')
os.rmdir(dir_name + 'Test/B')
os.rmdir(dir_name + 'Test\\C')
os.rmdir(dir_name + 'Test')

