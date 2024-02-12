import re
# Задания 6-8. Вариант 6.
# 6. Дана строка. Необходимо подсчитать количество чисел
# в этой строке, значение которых больше 5.

s = "f5j1s3k7429k42j2j63j145j3k4p9"

def moreThan5(s):
    nums = re.findall(r'\d+', s)
    print(nums)
    amount = 0
    for x in nums:
        if int(x) > 5:
            amount += 1
    return amount

print(moreThan5(s))