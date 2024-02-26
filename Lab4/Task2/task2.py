# Задание 2. Вариант 6. Дан файл, содержащий текст на русском языке.
# Определить, сколько раз встречается в нём самое длинное слово.

with open("text.txt", encoding="utf8") as textFile:
    text = textFile.read().split()
    mx = max(text, key=len)
    amount = text.count(mx)
    print(mx)
    print(amount)