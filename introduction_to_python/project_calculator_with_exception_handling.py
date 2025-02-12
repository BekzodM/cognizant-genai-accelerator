import logging

logging.basicConfig(filename='error_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def menu():
    print("Welcome to the Error-Free Calculator! Choose an option:")
    while True:
        try:
            user_choice = int(input("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit \n> "))
            if user_choice == 1:
                print("\n Addition \n")
                while True:
                    try:
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} + {num2} = {num1 + num2}")
                        break
                    except ValueError:
                        logging.info('Invalid input for addition.')
                        print("That's not a valid number! Please enter a valid number...")
                break
            elif user_choice == 2:
                print("\n Subtraction \n")
                while True:
                    try:
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} - {num2} = {num1 - num2}")
                        break
                    except ValueError:
                        logging.info('Invalid input for subtraction.')
                        print("That's not a valid number! Please enter a valid number...")
                break
            elif user_choice == 3:
                print("\n Multiplication \n")
                while True:
                    try:
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        print(f"{num1} * {num2} = {num1 * num2}")
                        break
                    except ValueError:
                        logging.info('Invalid input for multiplication.')
                        print("That's not a valid number! Please enter a valid number...")
                break
            elif user_choice == 4:
                print("\n Division \n")
                while True:
                    try:
                        num1 = int(input("Enter the first number: "))
                        num2 = int(input("Enter the second number: "))
                        result = num1/num2
                        print(f"{num1} / {num2} = {num1 / num2}")
                        break
                    except ValueError:
                        logging.info('Invalid input for division.')
                        print("That's not a valid number! Please enter a valid number...")
                    except ZeroDivisionError:
                        logging.info('Division by zero.')
                        print("Division by 0 is not allowed! Please try again...")
                break
            elif user_choice == 5:
                break
            else:
                print("Invalid input. Please enter a number from the menu...")
        except ValueError:
            print("Invalid input. Please enter a number from the menu...")

menu()