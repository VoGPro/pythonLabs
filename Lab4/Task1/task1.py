# Вариант 6. В файле набор чисел. Определить три таких числа, чтобы
# между ними было не менее К-1 чисел, а
# сумма этих чисел была минимально возможной. Запишите в ответе найденную
# сумму.
# Входные данные: Даны два входных файла: файл A (27-165a.txt) и
# файл B (27-165b.txt), каждый из которых в первой строке содержит
# число N – количество всех чисел,
# число К – минимальное количество чисел + 1, которое
# должно быть между числами.
# В каждой из следующих N строк находится одно число.
# Пример входного файла:
# 6 2
# 15
# 14
# 20
# 23
# 21
# 10
# При таких исходных искомая величина равна 45 – это сумма значений,
# зафиксированных на первой, третьей и шестой минутах измерений (15 + 20 + 10).
# В ответе укажите два числа: сначала искомое значение для файла А,
# затем для файла B.

def findMinSumOf3Nums(n, k, nums):
    min_sum1 = min_sum1_2 = min_sum1_2_3 = float('inf')
    for i in range(n - 2*k):
        min_sum1 = min(min_sum1, nums[i])
        min_sum1_2 = min(min_sum1_2, min_sum1 + nums[i + k])
        min_sum1_2_3 = min(min_sum1_2_3, min_sum1_2 + nums[i + 2*k])
    return min_sum1_2_3


# numbers1 = [5, 8, 2, 10, 15, 3, 7]
# k1 = 3
# numbers2 = [15, 14, 20, 23, 21, 10]
# k2 = 2
# result = findMinSumOf3Nums(len(numbers1), k1, numbers1)
# print(f"\nСумма: {result}")
# result = findMinSumOf3Nums(len(numbers2), k2, numbers2)
# print(f"\nСумма: {result}")

with open("27-165a.txt") as fileA:
    nk = fileA.readline().split()
    nk = [int(i) for i in nk]
    numbers = [int(num) for num in fileA.readlines()]
    result = findMinSumOf3Nums(nk[0], nk[1], numbers)
    print(f"\nСумма: {result}")

with open("27-165b.txt") as fileB:
    nk = fileB.readline().split()
    nk = [int(i) for i in nk]
    numbers = [int(num) for num in fileB.readlines()]
    result = findMinSumOf3Nums(nk[0], nk[1], numbers)
    print(f"\nСумма: {result}")
