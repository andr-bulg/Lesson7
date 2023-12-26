"""
Дана последовательность чисел (количество чисел может изменяться).
Используя форматированный вывод, выведите на экран количество чисел
в последовательности, а затем и сами числа.
Например, для чисел (2, 3, 5) вывод может иметь следующий вид:
“The 3 numbers are: 2, 3, 5.”
"""

# Решение через f-строки
k = (2, 3, 5)
length = len(k)

if length == 0:
    res_str = "Не задана последовательность чисел"
elif length == 1:
    res_str = f'The {length} number is: '
else:
    res_str = f"The {length} numbers are: "

for i in range(length):
    if i == length - 1:
        res_str += f'{k[i]}.'
    else:
        res_str += f'{k[i]}, '

print(res_str)

# Решение с использованием метода format()
k = (2,)
length = len(k)

if length == 0:
    res_str = "Не задана последовательность чисел"
elif length == 1:
    res_str = 'The {} number is: '.format(length)
else:
    res_str = 'The {} numbers are: '.format(length)

for i in range(length):
    if i == length - 1:
        res_str += '{}.'.format(k[i])
    else:
        res_str += '{}, '.format(k[i])

print(res_str)

# Решение с выводом в старом стиле
k = ()
length = len(k)

if length == 0:
    res_str = "Не задана последовательность чисел"
elif length == 1:
    res_str = 'The %d number is: ' % length
else:
    res_str = 'The %d numbers are: ' % length

for i in range(length):
    if i == length - 1:
        res_str += '%d.' % k[i]
    else:
        res_str += '%d, ' % k[i]

print(res_str)
