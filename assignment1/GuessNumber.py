import random
def guessNumber() :
    number = random.randrange(1, 25)
    print("The number is between 1 to 25")
    flag = False
    for i in range (5) :
        guess = int(input("Guess : "))

        if number == guess :
            print("Congratulation, You Won")
            flag = True
            break

        elif number < guess :
            print("hint : Number is smaller than your guess")

        else :
            print("hint : Number is greater than your guess")
        
        print(4 - i, " guesses are remaining.")

    if not flag :
        print("Sorry, you ran out of channce")
        print("Number was " , number)

    if(input("Do you want to try again?(y/n)") == "y") :
        guessNumber()


guessNumber()