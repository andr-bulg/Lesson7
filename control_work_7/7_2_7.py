"""
Дан список, состоящий из 4х элементов: ['apples', 1.3, 'oranges',  1.8].
Используя f-строки, выведите на экран следующую строку:
"The weight of an apple is 1.3, the weight of an orange is 1.8"
Измените f-строку таким образом, чтобы названия фруктов были напечатаны
в верхнем регистре, а их вес увеличился на 20%.
"""

s = ['apples', 1.3, 'oranges',  1.8]

print(f"The weight of an {s[0][:-1]} is {s[1]}, the weight of an {s[2][:-1]} is {s[3]}")

print(f"The weight of an {s[0][:-1].upper()} is {s[1] + s[1]*0.2}, "
      f"the weight of an {s[2][:-1].upper()} is {s[3] + s[3]*0.2}")


