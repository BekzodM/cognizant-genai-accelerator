print("Welcome to the Recursive Artistry Program!")
print("Choose an option:")

def menu():
    user_choice = int(input("1. Calculate Factorial \n2. Find Fibonacci \n3. Draw a Recursive Fractal \n4. Exit > "))
    while True:
        if user_choice == 1:
            factorial_num = int(input("Enter a number to find its factorial: "))
            print(f"Factorial of {factorial_num} is: {factorial(factorial_num)}")
            break
        elif user_choice == 2:
            fib_num = int(input("Enter a number to find nth fibonacci number: "))
            print(f"Fibonacci number of {fib_num} is: {fibonacci(fib_num)}")
            break
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            break

def factorial(num: int):
    if num < 1:
        return None
    if num == 1:
        return 1
    return num * factorial(num-1)


#recursive approach for fibonacci not very efficient.
def fibonacci(num: int):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

menu()