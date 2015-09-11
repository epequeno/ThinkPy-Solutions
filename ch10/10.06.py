# Write a function called remove_duplicates that takes a list and returns a
# new list with only the unique elements from the original. Hint: they don't
# have to be in the same order.

# Current Status: Complete

items = [1, 1, 2, 4, 5, 6, 7, 8, 8, 9, 10, 7]


def remove_duplicates(items):
    return list(set(items))

print remove_duplicates(items)

