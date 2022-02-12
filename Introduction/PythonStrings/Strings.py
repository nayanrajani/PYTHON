#Python Strings
"""
Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:
"""


print("Hello")
print('helloo')

# Assign String to a Variable ->
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "hello"
print(a)


# Multiline Strings ->
# You can assign a multiline string to a variable by using three quotes:
# Note: in the result, the line breaks are inserted at the same position as in the code.

a = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
# OR

b = '''
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
'''

print(a)
print(b)

"""
Strings are Arrays:

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

"""

a = "Hello, World!"
print(a[0])

"""
Looping Through a String:
Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""

for x in "banana":
    print(x)


# String Length
# To get the length of a string, use the len() function

a = "Hello Nayan, How are you? "
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = 'Yarr aaj mei free nahi hun, kal chale kya??'
print('kal' in txt)

# can be accessed using IF statement:

txt = 'Yarr aaj mei free nahi hun, kal chale kya??'

if 'kal' in txt:
    print("Yes, 'kal' is present")
else:
    print("No")


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)

# can be accessed using IF statement:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
