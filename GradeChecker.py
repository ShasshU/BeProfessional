print("Grade Checker")

grade = input("Enter your test score: ")

if grade > "90" or grade < "0":
    print("A or maybe error??")
elif grade <= "90" and grade >= "80" or grade == "85":
    print("You got B but maybe A??")
elif grade < "80" and grade >= "70" or not grade == "60":
    print("C?")
else:
    print("I don't know what your grade is sorry")