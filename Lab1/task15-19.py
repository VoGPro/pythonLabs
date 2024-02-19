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
# print(f"\n{a1}")
# print(move3Left(a1))
# print(f"\n{a2}")
# print(move3Left(a2))
# print(f"\n{a3}")
# print(move3Left(a3))


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

# print(f"\n{a1}")
# print(findBeforeMin(a1))
# print(f"\n{a2}")
# print(findBeforeMin(a2))
# print(f"\n{a3}")
# print(findBeforeMin(a3))


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

arr30 = [618, 107, 257, 324, 86, 432, 530]
print(f"\n{arr30}")
for i in range(len(arr30)):
    if isLocalMaxima(i, arr30):
        print(f"{arr30[i]} - локальный максимум")
    else:
        print(f"{arr30[i]} - не локальный максимум")