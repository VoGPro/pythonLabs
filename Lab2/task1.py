# Задание 1. Вариант 6. Количество слов в тексте.
# Дан текст: в первой строке записано число строк, далее идут сами
# строки. Определите, сколько различных слов содержится в этом тексте.

strings1 = ("4\n"
 "She sells sea shells on the sea shore;\n"
 "The shells that she sells are sea shells I'm sure.\n"
 "So if she sells sea shells on the sea shore,\n"
 "I'm sure that the shells are sea shore shells.")

def amountOfUniqueWords(strings):
    strings = strings.split()
    strings.pop(0)
    strings = set(strings)
    return len(strings)

print(f"\nКоличество различных слов: {amountOfUniqueWords(strings1)}")