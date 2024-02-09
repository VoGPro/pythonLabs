from math import sqrt
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
    while num != 0:
        if num % 10 < 3:
            amount += 1
        num //= 10
    return amount


# Функция 3. Найти количество чисел,
# не являющихся делителями исходного числа,
# не взамнопростых с ним и взаимно простых с суммой простых цифр этого числа.

def divisorsOf(num):
    divs = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            if num // i == i:
                divs.append(i)
            else:
                divs.append(i)
                divs.append(num // i)
    return divs

def sameElem(arr1, arr2):
    for x in arr1:
        for y in arr2:
            if x == y and x != 1 and y != 1:
                return True
    return False

# Функция 3.
def findAmountOfNums(num):
    sum = 0
    tmp = num
    while tmp != 0:
        if isPrime(tmp % 10):
            sum += tmp % 10
        tmp //= 10
    if sum == 0:
        return 0
    amount = 0
    numDivs = divisorsOf(num)
    for i in range(1, num):
        if num % i != 0:
            iDivs = divisorsOf(i)
            sumDivs = divisorsOf(sum)
            if sameElem(iDivs, numDivs) and not sameElem(sumDivs, iDivs):
                amount += 1
    return amount

# Example:
# 15
# sum: 5
# divs: 1 3 5 15
# not divs: 2 4 6 7 8 9 10 11 12 13 14
# not prime with num: 6 9 10 12
# prime with sum: 6 9 12
# amount: 3
