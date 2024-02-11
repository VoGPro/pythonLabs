import random
# Задания 2-4. Вариант 6.
# 6. Дана строка в которой записаны слова через пробел. Необходимо
# перемешать в каждом слове все символы в случайном порядке кроме первого
# и последнего.

sentence = "Дана строка в которой записаны слова через пробел"

def shuffleSymbs(sntc):
    words = sntc.split()
    newSntc = words[0] + ' '
    for i in range(1, len(words) - 1):
        l = list(words[i])
        random.shuffle(l)
        newSntc += ''.join(l) + ' '
    newSntc += words[-1]
    return newSntc


# 12. Дана строка в которой содержаться цифры и буквы. Необходимо
# расположить все цифры в начале строки, а буквы - в конце.

s = "ab51jk2n0fw3"

def separateNumsAbc(str):
    nums = ''
    abc = ''
    for char in str:
        if char.isalpha():
            abc += char
        elif char.isnumeric():
            nums += char
    newStr = nums + abc
    return newStr
