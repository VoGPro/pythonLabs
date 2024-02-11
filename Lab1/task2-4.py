import random
# Задания 2-4. Вариант 6.
# 6. Дана строка в которой записаны слова через пробел. Необходимо
# перемешать в каждом слове все символы в случайном порядке кроме первого
# и последнего.

s6 = "Дана строка в которой записаны слова через пробел"

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

s12 = "ab51jk2n0fw3"

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

def solveTask():
    pr = ("\n6. Дана строка в которой записаны слова через пробел. Необходимо\n"
           "перемешать в каждом слове все символы в случайном порядке кроме первого\n"
           "и последнего.\n\n"
           "12. Дана строка в которой содержаться цифры и буквы. Необходимо\n"
           "расположить все цифры в начале строки, а буквы - в конце.\n\n"
           "Чтобы решить задачу 6 - введите 6.\n"
           "Чтобы решить задачу 12 - введите 12.")
    print(pr)

    task = ''
    while not (task == '6' or task == '12'):
        task = input("Ввод: ")

    if task == '6':
        str6 = input("Введите строку (чтобы использовать строку по умолчанию введите 0): ")
        if str6 == '0':
            print("Ответ: " + shuffleSymbs(s6))
        else:
            print("Ответ: " + shuffleSymbs(str6))
    else:
        str12 = input("Введите строку (чтобы использовать строку по умолчанию введите 0): ")
        if str12 == '0':
            print("Ответ: " + separateNumsAbc(s12))
        else:
            print("Ответ: " + separateNumsAbc(str12))

    yn = input("\nРешить ещё задачу? (да/нет): ")

    if yn.lower() == "да":
        solveTask()


solveTask()
