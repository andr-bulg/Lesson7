"""
В файле nums.txt хранятся вещественные числа.
Дописать в файл эти же числа, упорядочив их по возрастанию.
"""

file_name = '../nums.txt'

with open(file_name, 'r') as f:
    nums = f.read()
nums = list(map(float, nums.split()))
nums.sort()
nums = ' '.join(list(map(str, nums)))

with open(file_name, 'a') as f:
    f.write(f'\n{nums}')

print('Запись в файл выполнена!')
