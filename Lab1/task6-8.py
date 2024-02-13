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

# print(moreThan5(s))


# 12. Дана строка. Необходимо найти те символы кириллицы,
# которые не задействованы в данной строке.

ruLetters = "глпщибпоыжактыяеоумршвалыфж"

def findLetters(s):
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о',
                'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    length = len(alphabet)
    i = 0
    while i < length:
        if s.count(alphabet[i]) > 0:
            del alphabet[i]
            i -= 1
            length -= 1
        i += 1
    return alphabet

print(findLetters(ruLetters))