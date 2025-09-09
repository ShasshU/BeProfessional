print("Welcome to the Grade Checker")

grade = input("Enter your test score: ") #asks the user their test score, and stores it in variable 'grade'

if grade.isdigit(): #ensure that the grade variable is an integer
    grade = int(grade)
else:
    print("Please enter a number between 0-100")    


if grade >= 90 and grade < 101: #checks if you scored a 90 or above
    print("Congratulations, you have an A in the class!")
elif grade < 90 and grade >= 80: #checks if you scored between a 80-89
    print("Congratulations, you have a B in the class! Put in a little more work and you can score an A!")
elif grade < 80 and grade >= 70: #checks if you scored between a 70-79
    print("Congratulations you scores a C! Push yourself a little more and you can do even better.")
elif grade < 70 and grade >= 60: #checks if you scored between a 60-69
    print("You scored a D! This isn't passing, so try your best to get it up")
elif grade < 60: #checks if you scored a 60 or below
    print("You scored an F. Study hard and try to get this score up!")
else: 
    print("Error")