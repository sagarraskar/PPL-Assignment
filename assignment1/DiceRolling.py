import random
def rollDice() :
    number = random.randrange(1, 6)
    return number

print("Welcome to Dice Roller(Type 'roll' to roll the dice and 'quit' to quit)")

while(True) :
    response = input()
    if response == "roll" :
        num = rollDice()
        print(num)

    elif response == "quit" :
        break

    else:
        print("invalid input")