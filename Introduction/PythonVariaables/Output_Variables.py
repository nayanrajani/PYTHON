
'''

Output Variables
The Python print statement is often used to output variables.

To combine both text and a variable, Python uses the + character:

'''

x = "Awesome"
print("python is " + x)

# You can also use the + character to add a variable to another variable:

x = "Python is "
y = "Awesome"

z = x + y

print(z)

# For numbers, the + character works as a mathematical operator:

x = 5
y = 10
print(x + y)

# if you try to combine String and a number, python will give you an error:

x = 5
y = "john"
print(x+y)