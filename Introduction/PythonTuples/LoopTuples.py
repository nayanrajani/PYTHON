# Using for loop
# loop through a tuple

tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x)

# loop through a index number

tuple1 = ("Nayan", "Mihir", "Ishwar")
for i in range(len(tuple1)):
    print(tuple1[i])

# Using While loop

tuple1 = ("Nayan", "Mihir", "Ishwar", "Tanay", "Shantanu")
i = 0
while i < len(tuple1):
    print(tuple1[i])
    i = i + 1
    


"""

Python - Loop Tuples
Loop Through a Tuple
You can loop through the tuple items by using a for loop.

Example
Iterate through the items and print the values:

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
Learn more about for loops in our Python For Loops Chapter.

Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.

Example
Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

"""