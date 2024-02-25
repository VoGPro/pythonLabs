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

def findMinSumOf3Nums(n, k, numbers):
    min_sum = float('inf')
    final_nums = []
    for i in range(n - 2*k):
        for j in range(i + k, n - k):
            for q in range(j + k, n):
                current_sum = numbers[i] + numbers[j] + numbers[q]
                if current_sum < min_sum:
                    min_sum = current_sum
                    final_nums = [numbers[i], numbers[j], numbers[q]]
    return final_nums


# numbers1 = [5, 8, 2, 10, 15, 3, 7]
# k1 = 3
# numbers2 = [15, 14, 20, 23, 21, 10]
# k2 = 2
# result = findMinSumOf3Nums(len(numbers1), k1, numbers1)
# print(f"\nТри числа с минимальной суммой: {result}\nСумма: {sum(result)}")

with open("27-165a.txt") as fileA:
    nk = fileA.readline().split()
    nk = [int(i) for i in nk]
    nums = [int(num) for num in fileA.readlines()]
    result = findMinSumOf3Nums(nk[0], nk[1], nums)
    print(f"\nТри числа с минимальной суммой: {result}\nСумма: {sum(result)}")

with open("27-165b.txt") as fileB:
    nk = fileB.readline().split()
    nk = [int(i) for i in nk]
    nums = [int(num) for num in fileB.readlines()]
    result = findMinSumOf3Nums(nk[0], nk[1], nums)
    print(f"\nТри числа с минимальной суммой: {result}\nСумма: {sum(result)}")
