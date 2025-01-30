#get user's age
#Handle exceptions when user enters an invalid input and asks to try again.
while True:
    try:
        age = int(input("How old are you? "))
        break       #Exit the while loop if entered a valid input
    except ValueError:
        print("Oops! Please enter a valid integer value. Try again...")
if age >= 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    #Check if only 1 year left and print "year" in singular form
    if 18-age == 1:
        print("Oops! You’re not eligible yet. But hey, only 1 more year to go!")
    else:
        print(f"Oops! You’re not eligible yet. But hey, only {18-age} more years to go!")
