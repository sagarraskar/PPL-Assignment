def isArmStrongNumber(number) :
    digits = []
    num = number

    while num != 0 :
        digits.append(num % 10)
        num = num // 10

    sum = 0
    n = len(digits)

    for i in range (0, n) :
        sum = sum + (digits[i] ** n)


    if int(sum) == number :
        return True

    return False

def getArmstrongNumbers(a, b) :
    armstrongNumbers = []
    for i in range(a, b + 1) :
        if isArmStrongNumber(i) :
            armstrongNumbers.append(i)

    return armstrongNumbers

print(getArmstrongNumbers(1, 1000))