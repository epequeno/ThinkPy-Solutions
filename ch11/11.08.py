# If you did Exercise 10.5, you already have a function named
# has_duplicates that takes a list as a parameter and returns True if
# there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

# Current Status: Complete

listOne = [1, 2, 3, 4, 5, 5]


def has_dups(myList):
    dictionary = {}
    for item in myList:
        dictionary[item] = 1 + dictionary.get(item, 0)
        if dictionary[item] > 1:
            return True
    return False

print has_dups(listOne)