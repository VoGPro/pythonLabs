# Задания 11-14. Вариант 6.
# 3. Отсортировать строки в порядке увеличения разницы между
# частотой наиболее часто встречаемого символа в строке и
# частотой его появления в алфавите.

def sortByFreq(args):
    def symbolsFreq(s):
        all_freq = {}
        for i in s:
            if i in all_freq:
                all_freq[i] += 1
            else:
                all_freq[i] = 1
        return all_freq

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

s3 = ["The United States of America (USA or U.S.A.) is a country primarily located in North America. It lies between Canada to the north and Mexico to the south.",
      "Russia (Russian: Россия, romanized: Rossiya, [rɐˈsʲijə]), or the Russian Federation, is a country spanning Eastern Europe and Northern Asia.",
      "China (Chinese: 中国; pinyin: Zhōngguó), officially the People's Republic of China (PRC), is a country in East Asia. It is the world's second-most-populous country.",
      "South Korea, officially the Republic of Korea (ROK), is a country in East Asia. It constitutes the southern part of the Korean Peninsula and borders North Korea.",
      "Japan (Japanese: 日本, [ɲihoɴ], Nippon or Nihon, and formally 日本国, Nippon-koku or Nihon-koku) is an island country in East Asia. It is in the northwest Pacific Ocean.",
      "The United Kingdom of Great Britain and Northern Ireland is a country in Northwestern Europe, off the north-western coast of the continental mainland.",
      "Germany, officially the Federal Republic of Germany, is a country in the western region of Central Europe. It is the second-most populous country in Europe after Russia.",
      "Italy (Italian: Italia, Italian: [iˈtaːlja]), officially the Italian Republic, is a country in Southern and Western Europe. Located in the middle of the Mediterranean Sea."]

print()
for string in s3:
    print(string)
print()

newS3 = sortByFreq(s3)

for string in newS3:
    print(string)
