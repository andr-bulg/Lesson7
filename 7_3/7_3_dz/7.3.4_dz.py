"""
В файле matrix.txt построчно хранится матрица целых чисел A(n,n).
Найти два наибольших простых числа.
Первое из них заменить минимальным элементом матрицы,
а второе - максимальным элементом. Записать полученную матрицу в файл result.txt.
"""

import functions_for_7_3_4and5 as func

A = []

file_name_1 = 'matrix.txt'
file_name_2 = 'result.txt'


with open(file_name_1, 'r') as f:
    A = func.read_matrix(f)

print('Исходная матрица:\n', A)

simple_numbers = []
for i in range(len(A)):
    for j in range(len(A[i])):
        if func.simple_number(A[i][j]):
            simple_numbers.append(A[i][j])

if len(simple_numbers) >= 2:
    simple_numbers.sort(reverse=True)


min_el, i_min, j_min = func.min_el_matrix(A)
max_el, i_max, j_max = func.max_el_matrix(A)

for i in range(len(A)):
    for j in range(len(A[0])):
        if A[i][j] == simple_numbers[0]:
            A[i][j] = min_el
            A[i_min][j_min] = simple_numbers[0]
        elif A[i][j] == simple_numbers[1]:
            A[i][j] = max_el
            A[i_max][j_max] = simple_numbers[1]

print('Новая матрица:\n', A)

with open(file_name_2, 'w') as f:
    func.write_matrix(A, f)

# with open(file_name_2, 'w') as f:
#     for row in A:
#         line = ' '.join(map(str, row))
#         f.write(line + '\n')

