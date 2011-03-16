# Write a function called is_sorted that takes a list as a parameter and 
# returns True if the list is sorted in ascending order and False otherwise.
# You can assume (as a precondition) that the elements of the list can be
# compared with the relational operators <, >, etc. For example, 
# is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should  
# return False.
#
listOne = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#listOne = [7, 3, 6, 10, 2, 8, 4, 1, 9, 5]

def is_sorted(listOne):
   print sorted(listOne) == listOne

is_sorted(listOne)

# Probably not what the book was after...
# http://wiki.python.org/moin/HowTo/Sorting/
