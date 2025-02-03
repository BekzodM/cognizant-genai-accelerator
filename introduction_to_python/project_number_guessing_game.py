"""
Simple number-guessing game!
1. Generate a random number
2. Prompt the User for Guesses
3. Count the Attempts
"""
import random

number_to_guess = random.randint(1, 100)
attempts = 0
while attempts < 10:
    input_number = int(input("Guess the number (between 1 and 100): "))
    if input_number == number_to_guess:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
    elif input_number < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    attempts += 1
if attempts > 10:
    print(f"You ran out of attempts :( The number was {number_to_guess}")