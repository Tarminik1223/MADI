import random
import numpy
import timeit

m = 50
n = 50
min_limit = -250
max_limit = 1012
strM = input("Введите строки: ")
if len(strM) > 0: m = int(strM)
strN = input("Введите стобцы: ")
if len(strN) > 0: n = int(strN)
while True:
    strMin_limit = input("Введите минимальное значение: ")
    if len(strMin_limit) > 0: min_limit = int(strMin_limit)
    strMax_limit = input("Введите максимальное значение: ")
    if len(strMax_limit) > 0: max_limit = int(strMax_limit)
    if min_limit <= max_limit:
        break
    else:
        print("\nМинимальный элемент не может быть больше максимального, повторите попытку\n")
# Создание матрицы
array = numpy.zeros((m, n))
# Заполнение матрицы
for i in range(m):
    for j in range(n):
        array[i][j] = random.randint(int(min_limit), int(max_limit))
print("Матрица сгенерирована: ")
print(array)


# Сортировка выбором
def SelectionSort(arr):
    """
    1)Найти наименьшее значение в списке.
    2)Записать его в начало списка, а первый элемент - на место, где раньше стоял наименьший.
    3)Снова найти наименьший элемент в списке. При этом в поиске не участвует первый элемент.
    4)Второй минимум поместить на второе место списка. Второй элемент при этом перемещается на освободившееся место.
    5)Продолжать выполнять поиcк и обмен, пока не будет достигнут конец списка.
    """
    new_array = arr.copy()
    for i in range(m):
        for j in range(n - 1):
            min = j
            for h in range(j + 1, n):
                if new_array[i][h] < new_array[i][min]:
                    min = h
            temp = new_array[i][j]
            new_array[i][j] = new_array[i][min]
            new_array[i][min] = temp
    return new_array


# Сортировка вставкой
def InsertionSort(arr):
    """
    1)Перебираются элементы в неотсортированной части массива.
    2)Каждый элемент вставляется в отсортированную часть массива на то место, где он должен находиться.

    """
    array = arr.copy()
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp = array[i][j]
            index = j
            while (temp < array[i][index - 1]) and (index > 0):
                array[i][index] = array[i][index - 1]
                index -= 1
            array[i][index] = temp
    return array


# Сортировка обменом
def BubbleSort(arr):
    """
    1)Попарно сравниваются элементы массива
    2)Если элемент слева* больше элемента справа, то элементы меняются местами
    3)Повторяем пункты 1-2 до тех пор, пока массив не отсортируется

    """
    array = arr.copy()
    for i in range(len(array)):
        for j in range(len(array[i])):
            for h in range(len(array[i]) - j - 1):
                if array[i][h + 1] < array[i][h]:
                    temp = array[i][h]
                    array[i][h] = array[i][h + 1]
                    array[i][h + 1] = temp
    return array


# Сортировка Шелла
def ShellSort(arr):
    """
    1)Сравниваются и сортируются значения, стоящие на растоянии d = половине длины массива.
    2)Процедура повторяется при d = d / 2
    3)После сортировки при d = 1 все элементы массива упорядочены
    """
    array = arr.copy()
    for i in range(len(array)):
        d = int(len(array[i]) / 2)
        while d > 0:
            for j in range(len(array[i])):
                for h in range(int(j + d), len(array[i]), d):
                    if array[i][j] > array[i][h]:
                        temp = array[i][j]
                        array[i][j] = array[i][h]
                        array[i][h] = temp

            d = int(d / 2)
    return array


# Сортировка Турнирная
def TournamentSort(array):
    """

    """
    arr = array.copy()
    for i in range(len(arr)):
        tournamentSort(arr[i])
    return arr


def tournamentSort(arr):
    tree = [None] * 2 * (len(arr) + len(arr) % 2)
    index = len(tree) - len(arr) - len(arr) % 2

    for i, v in enumerate(arr):
        tree[index + i] = (i, v)

    for j in range(len(arr)):
        n = len(arr)
        index = len(tree) - len(arr) - len(arr) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] is not None and tree[i + 1] is not None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] is not None else tree[i + 1]
            index -= n

        index, x = tree[0]
        arr[j] = x
        tree[len(tree) - len(arr) - len(arr) % 2 + index] = None


# Сортировка Быстрая
def QuickSort(array):
    """
    1)Выбрать элемент из массива. Назовём его опорным.
    2)Разбиение: перераспределение элементов в массиве таким образом, что элементы меньше опорного помещаются перед ним,
      а больше или равные после.
    3)Рекурсивно применить первые два шага к двум подмассивам слева и справа от опорного элемента.
      Рекурсия не применяется к массиву, в котором только один элемент или отсутствуют элементы.
    """
    arr = array.copy()
    for i in range(len(arr)):
        quickSort(0, len(arr[i]) - 1, arr, i)
    return arr


def quickSort(_first, _last, array, row):
    first = int(_first)
    last = int(_last)
    middle = int((first + last) / 2)

    while first < last:

        while array[row][first] < array[row][middle]:
            first += 1
        while array[row][last] > array[row][middle]:
            last -= 1
        if first <= last:
            array[row][first], array[row][last] = array[row][last], array[row][first]
            first += 1
            last -= 1

    if _first < last:
        quickSort(_first, last, array, row)
    if first < _last:
        quickSort(first, _last, array, row)


# Сортировка Пирамидальная
def heapify(arr, n, i):
    """
    1)Выстраиваем элементы массива в виде сортирующего дерева.
    2)Будем удалять элементы из корня по одному за раз и перестраивать дерево.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def HeapSort(array):
    arr = array.copy()
    for i in range(len(arr)):
        n = len(arr[i])

        for j in range(n, -1, -1):
            heapify(arr[i], n, j)

        for j in range(n - 1, 0, -1):
            arr[i][j], arr[i][0] = arr[i][0], arr[i][j]
            heapify(arr[i], j, 0)
    return arr


print("Время работы сортировки выбором: ")
start_time = timeit.default_timer()
print(SelectionSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки вставкой: ")
start_time = timeit.default_timer()
print(InsertionSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки обменом: ")
start_time = timeit.default_timer()
print(BubbleSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки Шелла: ")
start_time = timeit.default_timer()
print(ShellSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки Турнирной: ")
start_time = timeit.default_timer()
print(TournamentSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки Быстрой: ")
start_time = timeit.default_timer()
print(QuickSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)

print("Время работы сортировки Пирамидальной: ")
start_time = timeit.default_timer()
print(HeapSort(array))
time_2 = timeit.default_timer() - start_time
print(time_2)
