def generateDivisors(num) :
    divisors = []
    for i in range (1, int(num ** 0.5) + 1):
        if num % i == 0 :
            if num // i == i:
                divisors.append(i)

            else :
                divisors.append(i)
                divisors.append(num // i)
    return divisors

def findHarmonicMean(numbers) :
    sum = 0
    for i in range (0, len(numbers)) :
        sum = sum + (1 / numbers[i])

    mean = len(numbers) / sum
    return mean

def isHarmonicDivisor(number) :
    divisors = generateDivisors(number)
    mean = findHarmonicMean(divisors)

    if mean - int(mean) < 0.0000001 :
        return True

    return False

number = 1
harmonicDivisorNumbers = []
while len(harmonicDivisorNumbers) < 10 :
    if isHarmonicDivisor(number) :
        harmonicDivisorNumbers.append(number)
    number += 1

print(harmonicDivisorNumbers)

