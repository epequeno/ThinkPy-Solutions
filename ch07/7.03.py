# Exercise 7.3 To test the square root algorithm in this chapter, you could
# compare it with math.sqrt.
# Write a function named test_square_root that prints a table like this:
# [table]
# The first column is a number, a; the second column is the square root of a
# computed with the function from Exercise 7.2; the third column is the square
# root computed by math.sqrt; the fourth column is the absolute value of the
# difference between the two estimates.

# Current Status: Complete

import math


def newtons(n):
    n = float(n)  # convert input to float so printout() doesn't have to
    x = n / 2  # rough estimate
    i = 0
    while i < 10:
        y = (x + n / x) / 2  # newtons method
        x = y
        i += 1
    return y


def libmath(n):
    n = float(n)
    return math.sqrt(n)

# this function has a mix of int, str and float so there is a bit of
# conversion going on.


def printout():
    for i in range(1, 10):
        n = str(newtons(i))  # newtowns() gets int and returns float. change
        # to str.
        l = str(libmath(i))  # same here
        ab = abs(newtons(i) - libmath(i))  # out as int in as float, no str
        if (len(n) or len(l)) == 3:
            print i, n, '         ', l, '          ', ab
        elif len(n) == 12:
            print i, n, '', l, ' ', ab
        else:
            print i, n, l, '', ab

printout()