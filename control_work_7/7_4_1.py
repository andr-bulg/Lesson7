"""
Написать программу, которая создаст приведенное на рисунке image.png
дерево директорий и файлов.
Заполните файлы w.txt, f12.txt, f211.txt, f212.txt некоторым текстом.
Выполните обход созданного дерева снизу вверх,
а затем сверху вниз и выведите результаты на экран.
Выполните аналогичные действия для ветви с корнем в директории F3.
"""
import os
dir_name = 'C:/test_30122023/Work/'

# Создание конечной директории вместе с промежуточными рекурсивной функцией os.makedirs
# exist_ok=True - игнорирует ситуацию, когда конечная директория уже существует
os.makedirs(dir_name + 'F1/', exist_ok=True)
os.makedirs(dir_name + 'F2/F21/', exist_ok=True)
os.makedirs(dir_name + 'F3/F31/', exist_ok=True)
os.makedirs(dir_name + 'F3/F32/', exist_ok=True)


# Создание файлов в указанных директориях (папках)
with open(dir_name + 'w.txt', 'w') as f:
    f.write(f"Since you are learning Git, know that this has little to do with git \n"
    f"but with the text editor configured for use.\n")

f = open(dir_name + 'F1/f11.txt', 'w')
f.close()

with open(dir_name + 'F1/f12.txt', 'w') as f:
    f.write("Some text in file f12.txt\n")

f = open(dir_name + 'F1/f13.txt', 'w')
f.close()

with open(dir_name + 'F2/F21/f211.txt', 'w') as f:
    f.write("Some text in file f211.txt\n")

with open(dir_name + 'F2/F21/f212.txt', 'w') as f:
    f.write("Some text in file f212.txt\n")

f = open(dir_name + 'F3/F32/f321.txt', 'w')
f.close()

print("Обход созданного дерева снизу вверх:")
for root, dirs, files in os.walk(dir_name, topdown=False):
    print(f'Root: {root}')
    print(f'Subdirs: {dirs}')
    print(f'Files: {files}')
    print('--------------------------')


print("\nОбход созданного дерева сверху вниз:")
for root, dirs, files in os.walk(dir_name, topdown=True):
    print(f'Root: {root}')
    print(f'Subdirs: {dirs}')
    print(f'Files: {files}')
    print('--------------------------')


print("\nОбход снизу вверх для ветви с корнем в директории F3:")
for root, dirs, files in os.walk(dir_name + 'F3/', topdown=False):
    print(f'Root: {root}')
    print(f'Subdirs: {dirs}')
    print(f'Files: {files}')
    print('--------------------------')


print("\nОбход сверху вниз для ветви с корнем в директории F3:")
for root, dirs, files in os.walk(dir_name + 'F3/', topdown=True):
    print(f'Root: {root}')
    print(f'Subdirs: {dirs}')
    print(f'Files: {files}')
    print('--------------------------')

