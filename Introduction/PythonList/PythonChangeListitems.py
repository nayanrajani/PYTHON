# Change Item Value
# To change the value of a specific item, refer to the index number:

# Example
# Change the second item:

thislist = ["mango","orange","papaya"]
print(thislist)
print("Changing list now")
thislist[1] = "cherry"
print(thislist)

# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

lot1 = ["cherry", "mango", "orange", "papaya", "kiwi", "apple"]
lot1[1:3] = ["blackcurrant", "watermelon"]
print(lot1)

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:

lot1[1:2] = ["mango", "orange"] 
print(lot1)


"""
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:

"""

lot1[1:4] = ["watermelon"]
print(lot1)


"""
Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:
"""

lot2 = ["cherry", "banan", "watermelon"]
lot2.insert(2,"apple")
print(lot2)

# Note: As a result of the example above, the list will now contain 4 items.
