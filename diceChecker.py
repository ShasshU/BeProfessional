print("Dice Game Result Checker")

roll = input("Enter dice roll (1-6): ")

if roll == "6" or roll < "1" and roll > "6":
    print("You win big!")
elif roll == "3" and roll == "4" or roll == "5":
    print("You win something small.")
else:
    print("Lose maybe?? idk")