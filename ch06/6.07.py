# Exercise 6.7 A number, a, is a power of b if it is divisible by b and a/b
# is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b.

# Current Status: Complete

# I really couldn't figure this one out for the life of me so this solution
# is stolen directly from
# http://stackoverflow.com/questions/4429462/python-recursion-exercise

def is_power(a,b):
    if a == b:
        return False
    if(a%b != 0):
        return False
    elif(a/b == 1):
        return True
    else:
        return is_power(a/b,b)
