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


# Функция 2. Найти количество цифр числа, меньших 3.
def amountOf3(num):
    amount = 0
    while (num != 0):
        if (num % 10 < 3):
            amount += 1
        num //= 10
    return amount
