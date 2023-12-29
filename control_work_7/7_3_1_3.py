"""
Дан некоторый файл students.txt, который содержит список студентов
(имя и фамилия студента в каждой строке), отсортированный в алфавитном порядке.
Реализуйте следующую функцию:
 ⦁ редактировать информацию о студенте.
 Функция должна принимать 2 обязательных параметра: текущие имя и фамилия студента,
 и 2 опциональных параметра: новые имя или фамилия студента.
 Функция должна найти студента с заданными параметрами в списке и изменить его имя
 или фамилию (или и то, и другое в зависимости от переданных опциональных параметров),
 сохраняя сортировку списка. Если заданный студент в списке не найден,
 необходимо вывести на экран соответствующее сообщение.
"""

file_name = 'students.txt'

def student_replace(name, surname, new_name=None, new_surname=None):
    """
    Функция считывает список со студентами из файла в список temp,
    производит поиск по заданному имени и фамилии в этом списке.
    Если поиск завершается успешно, и заданы новое имя и/или новая фамилия,
    то заменяет старые данные на новые в найденной строке.
    Старые данные (строка) удаляются из общего списка temp, новые добавлятся.
    Производится сортировка списка по возрастанию.
    Далее выполняется очистка файла и новая запись всего списка temp в файл.

    :param name: имя
    :param surname: фамилия
    :param new_name: новое имя
    :param new_surname: новая фамилия
    :return: None
    """
    with open(file_name, 'r+') as f:
        # построчное считывание данных из списка в переменную temp
        # переменная temp является списком
        temp = f.readlines()
        s = f'{name.title()} {surname.title()}'
        total_flag = 0
        for line in temp:
            if s in line:
                temp_s = s
                total_flag = 1
                break

        if total_flag and new_name is None and new_surname is None:
            return

        elif total_flag:
            temp_s = s.split()

            flag = 0
            if new_name is not None:
                temp_s[0] = new_name
                flag = 1
            if new_surname is not None:
                temp_s[1] = new_surname
                flag = 1

            if flag:
                s2 = ' '.join(temp_s)
            temp.remove(f'{s}\n')
            temp.append(f'{s2}\n')
            temp.sort()

            with open(file_name, 'w') as f2:
                # запись обновлённого списка в файл, старые данные будут затёрты
                f2.writelines(temp)

        else:
            print(f"{s} отсутствует в списке студентов!")


# Проверка функции student_replace()
student_replace('Петр', 'Сергеев', new_name='Петро', new_surname='Сергиенко')
# student_replace('Петр', 'Сергеев')
# student_replace('Петр', 'Сергеев', new_name='Петро')
# student_replace('Петр', 'Сергеев', new_surname='Сергиенко')
student_replace('Камаз', 'Отходов', new_name='Петро', new_surname='Сергиенко')

