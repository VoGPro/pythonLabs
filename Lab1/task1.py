# Задание 1. Вариант 6.
# Функция 1. Найти сумму непростых делителей числа.

def isPrime(num):
    if num == 0 or num == 1:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Функция 1.
def sumOfNotPrimeDivs(num):
    i = 1
    sum = 0
    while i * i <= num:
        if num % i == 0:
            if num / i == i:
                if not isPrime(i):
                    sum += i
            else:
                if not isPrime(i):
                    sum += i
                if not isPrime(num / i):
                    sum += num / i
        i += 1
    return int(sum)
