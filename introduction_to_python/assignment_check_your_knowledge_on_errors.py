"""
Task 1 - Understanding Python Exceptions
Write a Python program that:

Prompts the user to enter a number.
Tries to divide 100 by the number.
Handles the following exceptions:
ZeroDivisionError (when dividing by zero).
ValueError (when the user enters non-numeric input).
Prints appropriate error messages for each exception.
"""

try:
    number = int(input("Enter a number: "))
    print(100/number)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")

"""
Task 2 - Types of Exceptions
Create a program that intentionally raises and handles the following exceptions:

IndexError by accessing an invalid list index.
KeyError by trying to access a non-existent key in a dictionary.
TypeError by adding a string and an integer.
Explain in comments how each error occurs and how it is handled.
"""

def invalid_index(idx):
    if idx > 3:
        raise IndexError("Index out of range.")

def invalid_key(key):
    dict = {}
    if key not in dict:
        raise KeyError("Key does not exist.")

def invalid_type(num):
    if not isinstance(num, int):
        raise TypeError("Can't add a string to an integer")
    

#invalid_index(4)
#invalid_key("color")
#invalid_type("hello")

"""
Task 3 - Using try...except...else...finally
Write a program that:

Prompts the user to enter two numbers.
Tries to divide the first number by the second number.
Implements the following:
try block to attempt the division.
except block to handle exceptions.
else block to display the result if no exceptions occur.
finally block to print a closing message regardless of exceptions.
"""
try:
    number = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = number/number2
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("You can't divide by zero!")
else:
    print(f"The result of the division is {result}")
finally:
    print("This block always executes. ")
