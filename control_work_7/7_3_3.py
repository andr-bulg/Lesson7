"""
Дано два бинарных файла. Напишите программу,
выполняющую слияние заданных файлов
(первая строка первого файла складывается с первой строкой второго файла и т.д.)
и записывающую результат в третий бинарный файл.
"""

file_name1 = 'nums_1.dat'
file_name2 = 'nums_2.dat'
file_name3 = 'nums_total.dat'

with open(file_name1, 'br') as f:
    a = f.read()

with open(file_name2, 'br') as f:
    b = f.read()

a = a.split()
b = b.split()
c = []

for i in range(len(a)):
    c.append(f'{a[i]} {b[i]}\n')

with open(file_name3, 'w') as f:
     f.writelines(c)

