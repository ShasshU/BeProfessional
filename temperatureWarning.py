print("Temperature Warning System")

temp = input("Enter temperature: ") # Asks the user for a temperature and stores it as a string

# Check if the input is a valid number
if temp.isdigit() or (temp.startswith('-')):
    temp = int(temp) # Convert the string to an integer
    
    # This code only runs if the input is a valid integer.
    # Handle the most extreme or specific cases first.
    if temp > 100:
        print("Warning: Too hot!")
    elif temp < 0:
        print("Warning: Too cold!")
    elif temp >= 50 and temp <= 100:
        print("The temperature is perfect")
    else:
        # This will catch temperatures between 0-49 degrees.
        print("The weather is okay")

else:
    # This runs if the input is not a number.
    print("Invalid input. Please enter a valid temperature")