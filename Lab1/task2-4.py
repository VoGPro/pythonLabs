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

print(shuffleSymbs(sentence))
