"""
Task 1 - Writing Functions
Create a function greet_user that accepts a name as a parameter and prints a personalized greeting.
Then, write another function add_numbers that takes two numbers as parameters, adds them, and returns the result.
"""
def greet_user(name):
    print(f"Hello, {name}! Welcome aboard.")

def add_numbers(num1, num2):
    return num1 + num2

greet_user("Bekzod")
add_numbers(18, 24)

"""
Task 2 - Using Default Parameters
Create a function describe_pet that accepts two parameters:

pet_name (string)
animal_type (string, default value is "dog").
The function should print a description of the pet.
"""
def describe_pet(pet_name:str, animal_type:str = "dog"):
    print(f"I have a {animal_type} named {pet_name}")

describe_pet("Bibiy")

"""
Task 3 - Functions with Variable Arguments
Write a function make_sandwich that accepts a variable number of arguments for sandwich ingredients and prints them as a list.

Example Output:
Making a sandwich with the following ingredients: - Lettuce - Tomato - Cheese
"""
def make_sandwich(*args):
    result = "Making a sandwich with the following ingredients:"
    for ingredient in args:
        result += f" - {ingredient}"
    print(result)

make_sandwich("Lettuce", "Tomato", "Cheese")

"""
Task 4 - Understanding Recursion
Write a recursive function factorial to calculate the factorial of a number.
Then, write another recursive function fibonacci to calculate the nth number in the Fibonacci sequence.

Example Output:
Factorial of 5 is 120. The 6th Fibonacci number is 8.
"""
def factorial(num: int):
    if num < 1:
        return None
    if num == 1:
        return 1
    return num * factorial(num-1)

print(f"Factorial of 5 is: {factorial(5)}")

#recursive approach for fibonacci not very efficient.
def fibonacci(num: int):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    
print(f"The 20th Fibonacci number is {fibonacci(20)}")