# If you did Exercise 10.5, you already have a function named 
# has_duplicates that takes a list as a parameter and returns True if 
# there is any object that appears more than once in the list.
# Use a dictionary to write a faster, simpler version of has_duplicates.

# Current Status: Complete

listOne = [1, 2, 3, 3, 4]

def has_dups(listOne):
   dictionary = {}
   for item in listOne:
       dictionary[item] = 1 + dictionary.get(item, 0)
       if dictionary[item] > 1:
           return True
   return dictionary

print has_dups(listOne)