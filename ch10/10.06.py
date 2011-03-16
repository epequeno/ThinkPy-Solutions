# Write a function called remove_duplicates that takes a list and returns a 
# new list with only the unique elements from the original. Hint: they don't
# have to be in the same order.
#
items = [1, 1, 2, 4, 5, 6, 7, 8, 8, 9, 10]

def remove_duplicates(items):
   newList = []
   for i in items:
       if items.count(i) > 1:
           if newList.count(i) < 1:
               newList.append(i)
       i += 1
   print items
   print newList
   
remove_duplicates(items)

# Not sure what the author was getting at by saying they don't have to be
# in order. By simply traversing the list, we can match the two conditions,
# that the item is a duplicate (>1) in items but does not already exist
# (<1) in newList. Once those conditions are met than we can append
# whatever i to newList.
