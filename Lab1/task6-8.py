import re
# Задания 6-8. Вариант 6.
# 6. Дана строка. Необходимо подсчитать количество чисел
# в этой строке, значение которых больше 5.

s6 = "f5j1s3k7429k42j2j63j145j3k4p9"

def moreThan5(s):
    nums = re.findall(r'\d+', s)
    print(nums)
    amount = 0
    for x in nums:
        if int(x) > 5:
            amount += 1
    return amount


# 12. Дана строка. Необходимо найти те символы кириллицы,
# которые не задействованы в данной строке.

s12 = "глпщибпоыжактыяеоумршвалыфж"

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


def solveTask():
    pr = ("\n6. Дана строка. Необходимо подсчитать количество чисел\n"
           "в этой строке, значение которых больше 5.\n\n"
           "12. Дана строка. Необходимо найти те символы кириллицы,\n"
           "которые не задействованы в данной строке.\n\n"
           "Чтобы решить задачу 6 - введите 6.\n"
           "Чтобы решить задачу 12 - введите 12.")
    print(pr)

    task = ''
    while not (task == '6' or task == '12'):
        task = input("Ввод: ")

    if task == '6':
        str6 = input("Введите строку (чтобы использовать строку по умолчанию введите 0): ")
        if str6 == '0':
            print("Строка по умолчанию: " + s6)
            print("Ответ: " + str(moreThan5(s6)))
        else:
            print("Ответ: " + str(moreThan5(str6)))
    else:
        str12 = input("Введите строку (чтобы использовать строку по умолчанию введите 0): ")
        if str12 == '0':
            print("Строка по умолчанию: " + s12)
            print("Ответ: " + str(findLetters(s12)))
        else:
            print("Ответ: " + str(findLetters(str12)))

    yn = input("\nРешить ещё задачу? (да/нет): ")

    if yn.lower() == "да":
        solveTask()


solveTask()