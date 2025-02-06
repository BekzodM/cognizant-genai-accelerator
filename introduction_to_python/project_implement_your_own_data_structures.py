# Inventory management program
inventory = {}
inventory["apple"] = (10, 2.5)
inventory["banana"] = (5, 1.2)
print("Welcome to the Inventory Manager!")
print("Current inventory:")
for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")
print("Adding a new item...")
while True:
    try:
        new_item_name = str(input("Please type new item name: "))
        break       #Exit the while loop if entered a valid input
    except ValueError:
        print("Oops! Please enter a valid string value. Try again...")
while True:
    try:
        new_item_quantity = int(input("Please type new item quantity: "))
        break       #Exit the while loop if entered a valid input
    except ValueError:
        print("Oops! Please enter a valid integer value. Try again...")
while True:
    try:
        new_item_price = float(input("Please type new item price (ex: 2.5): "))
        break       #Exit the while loop if entered a valid input
    except ValueError:
        print("Oops! Please enter a valid decimal value. Try again...")
inventory[new_item_name] = (new_item_quantity, round(new_item_price,1))
for item in inventory:
    print(f"Item: {item}, Quantity: {inventory[item][0]}, Price: ${inventory[item][1]}")

