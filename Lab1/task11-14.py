# Задания 11-14. Вариант 6.
# 3. Отсортировать строки в порядке увеличения разницы между
# частотой наиболее часто встречаемого символа в строке и
# частотой его появления в алфавите.

def symbolsFreq(s):
    all_freq = {}
    for i in s:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq
def sortByFreq(args):
    defaultStrings = []
    allStr = ''
    mcSymbs4Strings = [] # наиболее встречаемый символ и его частота для каждой строки
    for st in args:
        defaultStrings.append([st])
        st = st.replace(' ', '')
        allStr += st
        stFreq = symbolsFreq(st) # словарь для строки
        key_symbol = max(stFreq, key=stFreq.get) # наиболее встречаемый символ
        var_num = stFreq.get(key_symbol) # частота появления символа
        symb_n_freq = [key_symbol, var_num]
        mcSymbs4Strings.append(symb_n_freq) # добавляем символ с его частотой

    textFreq = symbolsFreq(allStr) # словарь символов и частоты для всех строк

    # Вычисление разницы между частотой наиболее встречаемого символа в строке и частотой его появления в алфавите
    for i in range(0, len(defaultStrings)):
        defaultStrings[i].append(textFreq.get(mcSymbs4Strings[i][0]) - mcSymbs4Strings[i][1])

    # Все символы в строках и их количество
    # print(textFreq)
    # Самый встречаемый символ в каждой строке
    # for mcSymb in mcSymbs4Strings:
    #     print(mcSymb)
    # print()

    # Строки до сортировки
    # for defStr in defaultStrings:
    #     print(defStr)
    # print()

    # сортировка строк в порядке увеличения разницы между частотами
    defaultStrings.sort(key=lambda x: x[1])

    # Строки после сортировки
    # for defStr in defaultStrings:
    #     print(defStr)
    # print()

    result = []
    for defStr in defaultStrings:
        result.append(defStr[0])

    return result

ts = ["The United States of America (USA or U.S.A.) is a country primarily located in North America. It lies between Canada to the north and Mexico to the south.",
      "Russia (Russian: Россия, romanized: Rossiya, [rɐˈsʲijə]), or the Russian Federation, is a country spanning Eastern Europe and Northern Asia.",
      "China (Chinese: 中国; pinyin: Zhōngguó), officially the People's Republic of China (PRC), is a country in East Asia. It is the world's second-most-populous country.",
      "South Korea, officially the Republic of Korea (ROK), is a country in East Asia. It constitutes the southern part of the Korean Peninsula and borders North Korea.",
      "Japan (Japanese: 日本, [ɲihoɴ], Nippon or Nihon, and formally 日本国, Nippon-koku or Nihon-koku) is an island country in East Asia. It is in the northwest Pacific Ocean.",
      "The United Kingdom of Great Britain and Northern Ireland is a country in Northwestern Europe, off the north-western coast of the continental mainland.",
      "France (French: [fʁɑ̃s]), officially the French Republic (French: République française [ʁepyblik fʁɑ̃sɛːz]), is a country located primarily in Western Europe.",
      "Germany, officially the Federal Republic of Germany, is a country in the western region of Central Europe. It is the second-most populous country in Europe after Russia.",
      "Italy (Italian: Italia, Italian: [iˈtaːlja]), officially the Italian Republic, is a country in Southern and Western Europe. Located in the middle of the Mediterranean Sea."]


# 6. Отсортировать строки в порядке увеличения медианного значения выборки строк (прошлое
# медианное значение удаляется из выборки и производится поиск нового медианного значения).

def sortByMed(strings):
    strings = sorted(strings, key=len)
    medWithStrings = []

    if strings and len(strings) % 2 != 0:
        s = strings.pop(len(strings) // 2)
        medWithStrings.append([len(s), s])

    while strings:
        s2 = strings.pop(len(strings) // 2)
        s1 = strings.pop(len(strings) // 2)
        medWithStrings.append([(len(s1) + len(s2)) / 2, s1, s2])

    medWithStrings.sort(key=lambda x: x[0])

    # for x in medWithStrings:
    #     print(f'\n{x[0]}')
    #     for i in range(1, len(x)):
    #         print(x[i])
    # print()

    stringsByMed = []
    for x in medWithStrings:
        for i in range(1, len(x)):
            stringsByMed.append(x[i])

    return stringsByMed


# 8. Отсортировать строки в порядке увеличения квадратичного отклонения между
# средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода
# тройки подряд идущих символов в строке.

def sortBySqrtDevOfWeigth(strings):
    def SqrtDev(s):
        avgWeigth = sum(ord(c) for c in s) / len(s)
        maxAvg3 = 0
        for i in range(len(s) - 2):
            avg = (ord(s[i]) + ord(s[i + 1]) + ord(s[i + 2])) / 3
            maxAvg3 = max(maxAvg3, avg)
        return (avgWeigth - maxAvg3) ** 2
    strings.sort(key=SqrtDev)
    return strings

s8 = ["zlrmdi", "sktx", "qcdfnda", "oewms", "sjfnm"]


# 12. Отсортировать строки в порядке увеличения квадратичного отклонения
# частоты встречаемости самого распространённого символа в наборе строк
# от частоты его встречаемости в данной строке.

def sortBySqrtDevOfFreq(args):
    defaultStrings = []
    allStr = ''
    mcSymbs4Strings = []
    for st in args:
        defaultStrings.append([st])
        st = st.replace(' ', '')
        allStr += st
        stFreq = symbolsFreq(st)
        key_symbol = max(stFreq, key=stFreq.get)
        var_num = stFreq.get(key_symbol)
        symb_n_freq = [key_symbol, var_num]
        mcSymbs4Strings.append(symb_n_freq)

    textFreq = symbolsFreq(allStr)

    for i in range(0, len(defaultStrings)):
        defaultStrings[i].append((textFreq.get(mcSymbs4Strings[i][0]) - mcSymbs4Strings[i][1])**2)

    defaultStrings.sort(key=lambda x: x[1])

    result = []
    for defStr in defaultStrings:
        result.append(defStr[0])

    return result


def solveTask():
    pr = ("\n3. Отсортировать строки в порядке увеличения разницы между\n"
          "частотой наиболее часто встречаемого символа в строке и\n"
          "частотой его появления в алфавите.\n\n"
          "6. Отсортировать строки в порядке увеличения медианного значения выборки строк (прошлое\n"
          "медианное значение удаляется из выборки и производится поиск нового медианного значения).\n\n"
          "8. Отсортировать строки в порядке увеличения квадратичного отклонения между\n"
          "средним весом ASCII-кода символа в строке и максимально среднего ASCII-кода\n"
          "тройки подряд идущих символов в строке.\n\n"
          "12. Отсортировать строки в порядке увеличения квадратичного отклонения\n"
          "частоты встречаемости самого распространённого символа в наборе строк\n"
          "от частоты его встречаемости в данной строке.\n\n"
          "Чтобы решить задачу 3 - введите 3.\n"
          "Чтобы решить задачу 6 - введите 6.\n"
          "Чтобы решить задачу 8 - введите 8.\n"
          "Чтобы решить задачу 12 - введите 12.")
    print(pr)

    task = ''
    while not (task == '3' or task == '6' or task == '8' or task == '12'):
        task = input("Ввод: ")

    if task == '3':
        print("\nСтроки до сортировки:")
        for string in ts:
            print(string)
        print("\nСтроки после сортировки:")
        newS3 = sortByFreq(ts)
        for string in newS3:
            print(string)
    elif task == '6':
        print("\nСтроки до сортировки:")
        for string in ts:
            print(string)
        print("\nСтроки после сортировки:")
        newS6 = sortByMed(ts)
        for string in newS6:
            print(string)
    elif task == '8':
        print(f"\nСтроки до сортировки:\n{s8}")
        print(f"\nСтроки после сортировки:\n{sortBySqrtDevOfWeigth(s8)}")
    else:
        print("\nСтроки до сортировки:")
        for string in ts:
            print(string)
        print("\nСтроки после сортировки:")
        newS12 = sortBySqrtDevOfFreq(ts)
        for string in newS12:
            print(string)

    yn = input("\nРешить ещё задачу? (да/нет): ")

    if yn.lower() == "да":
        solveTask()


solveTask()
