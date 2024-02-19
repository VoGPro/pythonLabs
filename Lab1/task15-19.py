# Задания 15-19. Вариант 6.
# 6. Дан целочисленный массив. Необходимо осуществить циклический
# сдвиг элементов массива влево на три позиции.

def move3Left(arr):
    if len(arr) <= 3:
        return arr
    temp = []
    for i in range(3):
        temp.append(arr.pop(0))
    arr.extend(temp)
    return arr

a1 = [4, 2, 5]
a2 = [6, 9, 0, 7]
a3 = [1, 3, 8, 5, 0]


# 18. Дан целочисленный массив. Необходимо найти элементы,
# расположенные перед первым минимальным.

def findBeforeMin(arr):
    beforeMin = []
    minValue = min(arr)
    i = 0
    while arr[i] != minValue:
        beforeMin.append(arr[i])
        i += 1
    return beforeMin


# 30. Дан целочисленный массив и натуральный индекс (число,
# меньшее размера массива). Необходимо определить, является
# ли элемент по указанному индексу локальным максимумом.

def isLocalMaxima(index, arr):
    n = len(arr)
    mx = []

    if (arr[0] > arr[1]):
        mx.append(0)

    for i in range(1, n - 1):
        if (arr[i - 1] < arr[i] > arr[i + 1]):
            mx.append(i)

    if (arr[-1] > arr[-2]):
        mx.append(n - 1)

    return index in mx

a3042 = [298, 107, 257, 324, 86, 432, 530]


# 42. Дан целочисленный массив. Найти все элементы, которые
# меньше среднего арифметического элементов массива.

def lessThanAvg(arr):
    avg = sum(arr) / len(arr)
    result = []
    for num in arr:
        if num < avg:
            result.append(num)
    return result


# 54. Для введённого списка построить список из элементов,
# встречающихся в исходном более трёх раз.

def amountMoreThan3(arr):
    unique = list(set(arr))
    amounts = []
    moreThan3 = []
    for x in unique:
        amounts.append(arr.count(x))
    for i in range(len(amounts)):
        if amounts[i] > 3:
            moreThan3.append(unique[i])
    return moreThan3

arr54 = ['x','s','x','r','e','y','x','p','e','y','w','t','u','n','x','s','t','t','r','e','r','t','s','u','e','w','t','p','s','u','n']


def solveTask():
    pr = ("\n6. Дан целочисленный массив. Необходимо осуществить циклический\n"
          "сдвиг элементов массива влево на три позиции.\n\n"
          "18. Дан целочисленный массив. Необходимо найти элементы,\n"
          "расположенные перед первым минимальным.\n\n"
          "30. Дан целочисленный массив и натуральный индекс (число,\n"
          "меньшее размера массива). Необходимо определить, является\n"
          "ли элемент по указанному индексу локальным максимумом.\n\n"
          "42. Дан целочисленный массив. Найти все элементы, которые\n"
          "меньше среднего арифметического элементов массива.\n\n"
          "54. Для введённого списка построить список из элементов,\n"
          "встречающихся в исходном более трёх раз.\n\n"
          "Чтобы решить задачу 6 - введите 6.\n"
          "Чтобы решить задачу 18 - введите 18.\n"
          "Чтобы решить задачу 30 - введите 30.\n"
          "Чтобы решить задачу 42 - введите 42.\n"
          "Чтобы решить задачу 54 - введите 54.")
    print(pr)

    task = ''
    while not (task == '6' or task == '18' or task == '30' or task == '42' or task == '54'):
        task = input("Ввод: ")

    if task == '6':
        print(f"\n{a1}")
        print(move3Left(a1))
        print(f"\n{a2}")
        print(move3Left(a2))
        print(f"\n{a3}")
        print(move3Left(a3))
    elif task == '18':
        print(f"\n{a1}")
        print(findBeforeMin(a1))
        print(f"\n{a2}")
        print(findBeforeMin(a2))
        print(f"\n{a3}")
        print(findBeforeMin(a3))
    elif task == '30':
        print(f"\n{a3042}")
        for i in range(len(a3042)):
            if isLocalMaxima(i, a3042):
                print(f"{a3042[i]} - локальный максимум")
            else:
                print(f"{a3042[i]} - не локальный максимум")
    elif task == '42':
        print(f"\n{a3042}")
        print(f"Меньше среднего арифметического: {lessThanAvg(a3042)}")
    else:
        print(f"\n{arr54}")
        print(f"Встречаются более трёх раз: {amountMoreThan3(arr54)}")

    yn = input("\nРешить ещё задачу? (да/нет): ")

    if yn.lower() == "да":
        solveTask()


solveTask()
