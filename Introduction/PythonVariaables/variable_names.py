"""
Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
"""

#  this are legal
myvar  = " john"
my_var = "john"
_my_var = "john"
myBar = "john"
MYVAR = "john"
myvar2 = "john"


#  this are illegal

'''
2myvar = "john"
my-var = 'john'
my var = "john"

'''

# Remember that variable names are case-sensitive

# Multi Words Variable Names
'''
There are several techniques you can use to make them more readable:
'''
# Camel Case

myVariableName = "john"

# pascal case

MyVariableName = "john"

# snake case

my_variable_name = "john"