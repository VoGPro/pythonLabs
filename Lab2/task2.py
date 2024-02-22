# Задание 2. Вариант 6. Частотный анализ.
# Дан текст: в первой строке записано количество строк в тексте, а затем
# сами строки. Выведите все слова, встречающиеся в тексте, по одному на
# каждую строку. Слова должны быть отсортированы по убыванию их
# количества появления в тексте, а при одинаковой частоте появления - в
# лексикографическом порядке.

strings2 = ("9\n"
            "hi\n"
            "hi\n"
            "what is your name\n"
            "my name is bond\n"
            "james bond\n"
            "my name is damme\n"
            "van damme\n"
            "claude van damme\n"
            "jean claude van damme\n")

def wordsFreq(arr):
    all_freq = {}
    for i in arr:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1
    return all_freq

def sortWordsByFreq(strings):
    strings = strings.split()
    strings.pop(0)
    all_freq = {}
    for i in strings:
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    strings.clear()
    for item in all_freq:
        strings.append((all_freq.get(item), item))

    strings.sort(key=lambda x: x[1])
    strings.sort(key=lambda x: x[0], reverse=True)

    sorted_strings = []
    for item in strings:
        sorted_strings.append(item[1])

    return sorted_strings

strings2_sorted = sortWordsByFreq(strings2)
print()
for s in strings2_sorted:
    print(s)