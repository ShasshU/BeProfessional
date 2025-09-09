print("Dice Game Result Checker")

roll = input("Enter a dice roll (1-6): ")

# First checks if the input is a valid digit.
if roll.isdigit():
    # If it is a digit, convert the string to an integer.
    roll = int(roll)
    
    #only runs if roll is an integer
    if roll >= 1 and roll <= 6: #checks if its between 1-6
        # Check the winning and losing conditions.
        if roll == 6:
            print("You win big!")
        elif roll >= 3 and roll <= 5:
            print("You win something small")
        else: # This handles rolls of 1 and 2.
            print("You lose")
    else:
        # This handles numbers outside the 1-6 range.
        print("Invalid roll. Please enter a number between 1 and 6.")

else:
    # This handles any input that is not a digit
    print("Invalid input. Please enter a valid number.")