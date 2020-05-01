import random

for x in range(0,3):
    def rollDice():
        dice = [1,2,3,4,5,6]
        new = random.choice(dice)

        print("Your new number is:",new)
        
    print("Type start to roll the dice!")
    x = input()

    if x == "start":
        rollDice()
    else:
        print("Enter a valid input!")
