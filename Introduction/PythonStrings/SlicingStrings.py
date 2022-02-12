# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Getoutfromhere"

print(b[2:7])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:

b = "what are you doing"
print(b[:8])


# Slice To the End
# By leaving out the end index, the range will go to the end:

b = "it is not my type"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])