"""
Task 1 - Working with Lists

Create a list of your favorite fruits. Add at least five fruits to the list.
Perform the following operations:
Append a new fruit to the list.
Remove one fruit from the list using the remove() method.
Print the list in reverse order using slicing.
Example Output:

Original list: ['apple', 'banana', 'cherry', 'date', 'elderberry']
After adding a fruit: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
After removing a fruit: ['banana', 'cherry', 'date', 'elderberry', 'fig']
Reversed list: ['fig', 'elderberry', 'date', 'cherry', 'banana']
"""
favorite_fruits = ['banana', 'blackberry', 'date', 'mango', 'peach']
print(f"Original list: {favorite_fruits}")
favorite_fruits.append('strawberry')
print(f"After adding a fruit: {favorite_fruits}")
favorite_fruits.remove('mango')
print(f"After removing a fruit: {favorite_fruits}")
print(f"Reversed list: {favorite_fruits[::-1]}")

"""
Task 2 - Exploring Dictionaries

Create a dictionary to store information about yourself with the following keys: "name", "age", "city".
Add a new key-value pair to the dictionary for "favorite color".
Update the "city" key with a new value.
Print all the keys and values using a loop.
Example Output:

Keys: name, age, city, favorite color
Values: Alice, 25, New York, Blue
"""
about_me = {
    "name" : "Bekzod",
    "age" : 22,
    "city" : "New York City",
}
about_me["favorite color"] = "Green"
print(about_me)
about_me["city"] = "Boston"
keys = []
values = []
for key in about_me:
    keys.append(key)
    values.append(about_me[key])
print(f"Keys: {keys}")
print(f"Values: {values}")

"""
Task 3 - Using Tuples

Create a tuple with three elements: your favorite movie, song, and book.
Try to change one of the elements (you’ll see why tuples are immutable!).
Print the length of the tuple using the len() function.
Example Output:

Favorite things: ('Inception', 'Bohemian Rhapsody', '1984')
Oops! Tuples cannot be changed.
Length of tuple: 3
"""
my_tuple = ("Interstellar", "NA", "Programming Python: Powerful Object-Oriented Programming 😁")
try:
    my_tuple[2] = "Jk"
except:
    print("Oops! Tuples cannot be changed.")
print(f"Length of tuple: {len(my_tuple)}")