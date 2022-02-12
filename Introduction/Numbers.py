"""

Python Numbers
There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them:

"""

x = 1          #int
y = 2.8        #float
z = 1j         #complex

print(type(x))
print(type(y))
print(type(z))

# Int ->
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 49841326863651365658
z = -464646

print(type(x))
print(type(y))
print(type(z))

# Float ->
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.144
y = 498.15
z = -46.54

print(type(x))
print(type(y))
print(type(z))

# Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 14e4
y = 49E1
z = -46.5e4

print(type(x))
print(type(y))
print(type(z))

print((x))
print((y))
print((z))

# Complex ->
# Complex numbers are written with a "j" as the imaginary part:


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

print(x)
print(y)
print(z)

# Type Conversion ->
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

#Note: You cannot convert complex numbers into another number type.


print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Random Number ->
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random

print(random.randrange(1,100))

