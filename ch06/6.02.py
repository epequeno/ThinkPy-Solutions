# Exercise 6.2 Use incremental development to write a function called
# hypotenuse that returns the length of the hypotenuse of a right triangle
# given the lengths of the two legs as arguments. Record each stage of the
# development process as you go.

# Current Status: Complete

import math


def hypotenuse(x, y):
    return math.sqrt(x ** 2 + y ** 2)

print hypotenuse(3, 4)

"""pretty much just wrote this out with one try (coming back to this problem
after having done the rest of the book). I did forget to import math the first
time around though so this took two revisions"""