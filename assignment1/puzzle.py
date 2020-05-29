import numpy
dictionary = {1 : "grass", 2 : "goat", 4 : "tiger"}
grass = 1
goat = 2
tiger = 4
inleftbank = False
inrightbank = True
rightbank = [tiger,grass,goat]
leftbank = []
boat = 0

def ispossible(array) :
    sum = 0
    for i in array :
        sum += i
    if sum == 3 or sum == 6 :
        return False

    return True


def arraysum(array) :
    sum = 0
    for i in array :
        sum += i
    return sum

boat = 0
while arraysum(leftbank) != 7:
    if(inrightbank) :
        if boat != 0 :
            rightbank.append(boat)
            boat = 0

        boat = rightbank.pop(0)
        if(ispossible(rightbank) and ispossible(leftbank)) :
            inleftbank = True
            inrightbank = False
            print("Move ", dictionary[boat], " to left bank")

        else :
            rightbank.append(boat)
            boat = 0

    if(inleftbank) :
        leftbank.append(boat)
        boat = 0

        if(ispossible(leftbank)) :
            pass

        else:
            boat = leftbank.pop(0)
            print("Move ", dictionary[boat], " to right bank")
        inleftbank = False
        inrightbank = True







