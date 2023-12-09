"""
Вывести на экран содержимое созданного в предыдущей задаче двоичного файла.
"""
file_name = 'nums.dat'
with open(file_name, 'r') as f:
    print(f.read())

