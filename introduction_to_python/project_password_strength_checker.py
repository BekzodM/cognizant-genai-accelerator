password = str(input("Please enter your password: "))
isLong = False
contains_upper = False
contains_lower = False
contains_digit = False
contains_special_char = False
password_strength = 10
if len(password) >= 8:
    isLong = True
for char in password:
    if char.isupper():
        contains_upper = True
    elif char.islower():
        contains_lower = True
    if char.isdigit():
        contains_digit = True
    if char.isascii() and not char.isalnum():
        contains_special_char = True

if isLong and contains_upper and contains_lower and contains_digit and contains_special_char:
    print("Your password is strong! 💪")
    print(f"Password strength: {password_strength}")
else:
    print("Your password needs the following: ")
    if not isLong:
        password_strength -= 2
        print("At least 8 characters")
    if not contains_upper:
        password_strength -= 2
        print("At least one uppercase letter")
    if not contains_lower:
        password_strength -= 2
        print("At least one lowercase letter")
    if not contains_digit:
        password_strength -= 2
        print("At least one digit (0-9)")
    if not contains_special_char:
        password_strength -= 2
        print("At least one special character")
    print(f"Password strength: {password_strength}")