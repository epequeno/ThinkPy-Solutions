# Write a function called chop that takes a list and modifies it, removing the
# first and last elements, and returns None.
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements.
#
# I don't know how to get this to produce None but getting rid of first and
# last elements works. This is really middle().

# Current Status: Complete

nom = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def chop(nom):
    del nom[0]
    del nom[-1]
    print nom

print chop(nom)


def middle(nom):
    t = nom[1:-1]
    return t

print middle(nom)