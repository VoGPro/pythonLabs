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

print(f"\n{a1}")
print(findBeforeMin(a1))
print(f"\n{a2}")
print(findBeforeMin(a2))
print(f"\n{a3}")
print(findBeforeMin(a3))