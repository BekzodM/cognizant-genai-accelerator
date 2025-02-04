"""
Task 1 - String Slicing and Indexing

Create a string variable with the value "Python is amazing!".
Extract the following using slicing:
The first 6 characters ("Python")
The word "amazing"
The entire string in reverse order
Print each of these slices with a clear label.
Example Output:

First word: Python
Amazing part: amazing
Reversed string: !gnizama si nohtyP
"""
my_string = "Python is amazing!"
print(f"First word: {my_string[:6]}")
print(f"Amazing part: {my_string[10:-1]}")
print(f"Reversed string: {my_string[::-1]}")

"""
Task 2 - String Methods

Create a string with the value " hello, python world! ".
Use the following string methods and print the results:
strip() to remove extra spaces
capitalize() to capitalize the first letter
replace() to replace "world" with "universe"
upper() to convert the string to uppercase
"""
my_string = " hello, python world! "
print(f"My string with extra spaces removed: {my_string.strip()}")
print(f"My string with first letter capitalized: {my_string.strip().capitalize()}")
print(f"""My string with "world" replaced with "universe": {my_string.replace("world", "universe")}""")
print(f"My string converted to uppercase: {my_string.upper()}")

"""
Task 3 - Check for Palindromes
Write a Python program to check if a string is a palindrome (reads the same backward and forward).

Ask the user to input a word.
Use slicing to reverse the string and compare it with the original.
Print a friendly message indicating whether the word is a palindrome.
Example Run:

Enter a word: madam
Yes, 'madam' is a palindrome!
"""
word = input("Please enter a word to check if it's a palindrome: ")
if word[::-1] == word:
    print(f"Yes, {word} is a palindrome!")
else:
    print(f"No, {word} is not a palindrome.")