# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

'''
age = 23
txt = "My name is Nayan, I am " + age + "Years old"
print(txt)   #Error

'''

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:

age = 23
txt = "My name is Nayan, and I'm {} Years old"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 5
itemno = 1001
price = 101.05
myorder = "I want {} pieces of item {} for {} Rupees"
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 5
itemno = 1001
price = 101.05
myorder = "I want to pay {2} Rupees for {0} pieces of item {1}. "
print(myorder.format(quantity, itemno, price))

