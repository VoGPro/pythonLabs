# Задание 9. Прочитать список строк с клавиатуры.
# Упорядочить по длине строки.

print("Следующие 5 строк будут упорядочены по длине.\nВведите 5 строк.")
strings = []
for i in range(1, 6):
    strings.append(input(f"Ввод {i}: "))

print(sorted(strings, key=len))