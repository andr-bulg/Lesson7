"""
Создать двоичный файл nums.dat и записать в него целое число n,
а затем в следующей строке n вещественных чисел.
"""
file_name = 'nums.dat'
n = int(input('Введите целое число n от 1 до 5: '))
nums = [1.5, 7.234, 4.61, 0.7, 124.4]

with open(file_name, 'w') as f:
     if 1 <= n <= 5:
          f.write(str(n)+'\n')
          for i in range(n):
               f.write(f'{nums[i]} ')
     else:
          print('Неверно задано число n!')
