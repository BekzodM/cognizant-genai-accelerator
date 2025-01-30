"""
Task 1 - Variables: Your First Python Intro
Let’s start simple! Imagine you’re describing yourself (or anyone else you like) using Python variables.

Create a name variable that stores a string (like your name or a fictional character’s name).
Create an age variable that stores an integer value.
Create a height variable that stores a floating-point number.
For example, something like this:

name = "Alex"
age = 25
height = 5.9
Now print these variables in a friendly message:

Example Output: "Hey there, my name is Alex! I’m 25 years old and 5.9 feet tall."
Feel free to get creative with the message!
"""
name = "not Bekzod"
age = 20
height = 5.87
print(f"Hi, my name is {name}! I have a friend that is {age} years old. "\
      f"This friend of mine has another friend that is {height} feet tall.")

"""
Task 2 - Operators: Playing with Numbers
We all love some math, don’t we? Okay, maybe not everyone, but trust me, this will be easy and fun!

Pick two numbers, let’s say num1 and num2 (you choose the values!).
Perform the following operations on these numbers:
Addition
Subtraction
Multiplication
Division
Write your Python code to calculate and display the results with a nice message for each.
For example:

num1 = 10
num2 = 3
print("The sum of 10 and 3 is", num1 + num2)
Be sure to explain what you’re doing in comments! Bonus points if you throw in some humor.
"""
num1 = 184
num2 = 23
print(f"The sum of {num1} and {num2} is {num1+num2}")
print(f"The difference of {num1} and {num2} is {num1-num2}")
print(f"The product of {num1} and {num2} is {num1*num2}")
print(f"{num1} divided by {num2} is {num1/num2}")

"""
Task 3 - Conditional Statements: The Number Checker
Now for the real challenge: let’s make your code think!

Write a program that takes a number from the user and tells them whether it’s positive, negative, or zero.
Here’s how it should work:

Ask the user to enter a number (use the input() function).
Use if, elif, and else statements to check:
If the number is greater than 0, print: "This number is positive. Awesome!"
If the number is less than 0, print: "This number is negative. Better luck next time!"
If the number is exactly 0, print: "Zero it is. A perfect balance!"
Make sure to test your code with a few different numbers. You’ll be surprised how fun it is to see your program come to life!
"""
num = input("Please enter a number: ")
if int(num) > 0:
    print("The number you entered is a positive number.")
elif int(num) < 0:
    print("The number you entered is a negative number.")
else:
    print("The number you entered is zero.")
