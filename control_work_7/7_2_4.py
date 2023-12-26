"""
Дан кортеж, состоящий из 4х элементов: (2, 123.4567, 10000, 12345.67).
Используя метода format() и f-строки, преобразуйте данные значения в следующую строку:
'File_002 :      123.46,  1.00e+04,  1.23e+04'
"""
k = (2, 123.4567, 10000, 12345.67)

print("Форматированный вывод методом format(): ")
print('File_{:>03d} :{:>12.2f}, {:.2e}, {:.2e}'.format(*k))

print("\nФорматированный вывод через f-строку: ")
print(f"File_{k[0]:>03d} :{k[1]:>12.2f}, {k[2]:.2e}, {k[3]:.2e}")
