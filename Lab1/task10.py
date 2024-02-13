# Задание 10. Дан список строк с клавиатуры.
# Упорядочить по количеству слов в строке.

print("Следующие 5 строк будут упорядочены по количеству слов в строке.\nВведите 5 строк.")
strings = []
for i in range(1, 6):
    strings.append(input(f"Ввод {i}: "))

strings.sort(key=lambda x: len(x.split()))

print(strings)