def simple_number(num):
    """
    Функция определяет простое число.
    :param num: число.
    :return: возвращает True, если число простое.
    """
    if num <= 1:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

def min_el_matrix (m):
    """
    Функция определяет минимальный элемент в матрице.
    :param m: матрица.
    :return: возвращает минимальный элемент и его индексы.
    """
    min_el = m[0][0]
    i_min = j_min = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] < min_el:
                min_el = m[i][j]
                i_min = i
                j_min = j
    return min_el, i_min, j_min

def max_el_matrix (m):
    """
    Функция определяет максимальный элемент в матрице.
    :param m: матрица.
    :return: возвращает максимальный элемент и его индексы.
    """
    max_el = m[0][0]
    i_max = j_max = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] > max_el:
                max_el = m[i][j]
                i_max = i
                j_max = j
    return max_el, i_max, j_max

def read_matrix(f):
    """
    Функция чтения матрицы из текстового файла.
    :param f: файловый объект.
    :return: возвращает числовую матрицу.
    """
    m = []
    # Определение количества строк в файле
    n = len(f.readlines())
    # Перемещение условного курсора в начало файла
    f.seek(0)
    for row in range(n):
        # Считывание очередной строки из файла
        line = f.readline()
        # Преобразование строки в список с числами
        # метод split() преобразует строку в список с элементами типа str
        # функция map() преобразует список в список с числовыми элементами
        nums = list(map(int, line.split()))
        m.append(nums)
    return m

def write_matrix(m, f):
    """
    Функция записи числовой матрицы в текстовый
    :param m: матрица.
    :param f: файловый объект.
    :return: None
    """
    for row in m:
        # Преобразование числового списка в строку
        # функция map() преобразует список с числовыми элементами в список
        # с элементами типа str
        # метод join() преобразует список с элементами типа str в строку
        line = (' '.join(map(str, row)) + '\n')
        f.write(line)
    print('Матрица успешно записана в файл!')

def sr_arithmetic_of_matrix(m):
    """
    Функция вычисляет среднее арифметическое каждой строки матрицы.
    :param m: матрица.
    :return: кортеж, содержащий среднее арифметическое каждой строки матрицы.
    """
    k = []
    for row in m:
        k.append(round(sum(row)/len(row), 2))
    return tuple(k)

def count_negative_elements(m):
    """
    Функция вычисляет количество отрицательных элементов в каждом столбце матрицы.
    :param m: матрица.
    :return: кортеж, содержащий количество отрицательных элементов каждого столбца матрицы.
    """
    k = []
    for i in range(len(m[0])):
        count = 0
        for j in range(len(m)):
            if m[j][i] < 0:
                count += 1
        k.append(count)
    return tuple(k)

# Тестирование функций
if __name__ == '__main__':

    some_matrix = [[2, -3],
                   [15, 7]]

    print(simple_number(4))
    print(simple_number(-1))
    print(simple_number(1))
    print(simple_number(7))
    print(min_el_matrix(some_matrix))
    print(max_el_matrix(some_matrix))
    print(sr_arithmetic_of_matrix(some_matrix))
    print(count_negative_elements(some_matrix))



