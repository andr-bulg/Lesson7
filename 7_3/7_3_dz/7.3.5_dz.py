"""
В файле matrix.txt построчно хранится матрица C(k,m).
Сформировать вектор D=(d1, d2, d3, …, dk),
каждый элементы которого представляет собой среднее арифметическое элементов
строк матрицы С, и вектор G=(g1, g2, g3, …, gm), каждый элемент которого
равен количеству отрицательных элементов столбцов матрицы С.
Записать полученные векторы в соответствующие файлы vectorD.txt и vectorG.txt.
"""

import functions_for_7_3_4and5 as func

file_name = ['matrix2.txt', 'vectorD.txt', 'vectorG.txt']

C = []

with open(file_name[0], 'r') as f:
    C = func.read_matrix(f)

print('Исходная матрица:\n', C)

D = func.sr_arithmetic_of_matrix(C)
G = func.count_negative_elements(C)

with open(file_name[1], 'w') as f:
    f.write('D=' + str(D))

with open(file_name[2], 'w') as f:
    f.write(f'G={G}')

