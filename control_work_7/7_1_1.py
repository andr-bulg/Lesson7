"""
Напишите программу, которая спрашивала бы у пользователя его имя,
пол, возраст и место жительства, а затем выводила бы полученную информацию
на экран в следующем формате:
This is [name].
He (she) is [age] years old.
He (she) lives in [city].
"""

name = input("Введите своё имя: ")
sex = input("Введите свой пол: ")
age = int(input("Введите свой возраст: "))
city = input("Введите своё место проживания: ")

print(f'This is {name.title()}.')
if sex[0] in ('М', 'м', 'M', 'm'):
    print(f'He is {age} years old.')
    print(f'He lives in {city.title()}.')
else:
    print(f'She is {age} years old.')
    print(f'She lives in {city.title()}.')

