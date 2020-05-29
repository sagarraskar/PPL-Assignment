def generateProperDivisors(num) :
    divisiors = []
    for i in range (1, int(num ** 0.5) + 1):
        if num % i == 0 :
            if num // i == i:
                divisiors.append(i)

            else :
                divisiors.append(i)
                divisiors.append(num // i)
    divisiors.remove(num)
    return divisiors

def getSum(array) :
    sum = 0
    for i in array :
        sum = sum + i
    return sum


def areAmicableNumbers(num1, num2) :
    divisiors1 = generateProperDivisors(num1)
    divisiors2 = generateProperDivisors(num2)

    sum1 = getSum(divisiors1)
    sum2 = getSum(divisiors2)

    if(sum1 == num2 and sum2 == num1 and num1 != num2) :
        return True

    return False


pair = ()
pairs = []
checked = []
i = 1
while(len(pairs) < 10) :
    flag = True
    for j in checked :
        if(j == i) :
            flag = False
    j = getSum(generateProperDivisors(i))
    if(j != 0 and  flag) :
        if(areAmicableNumbers(i, j)) :
            pair = (i, j)
            checked.append(i)
            checked.append(j)
            pairs.append(pair)

    i += 1
print(pairs)


