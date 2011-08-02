# Fermat's Last Theorem says that there are no integers a, b, and c such that
# a^n + b^n = c^n
# for any values of n greater than 2.
# 1. Write a function named check_fermat that takes four parameters-a, b, c 
# and n-and that checks to see if Fermat's theorem holds. If n is greater than 
# 2 and it turns out to be true that a^n + b^n = c^n
# the program should print, "Holy smokes, Fermat was wrong!" Otherwise the
# program should  print, "No, that doesn't work."
# 2. Write a function that prompts the user to input values for a, b, c and n,
# converts them to integers, and uses check_fermat to check whether they 
# violate Fermat's theorem.

a = int(raw_input('What value to use for a?\n'))
b = int(raw_input('What value to use for b?\n'))
c = int(raw_input('What value to use for c?\n'))
n = int(raw_input('What value to use for n?\n'))

def check_fermat(a, b, c, n):
    if n == 2:
       print 'Pythagoras got that one already, thanks.\n'
    elif a**n + b**n == c**n:
        print('Holy Smokes, Fermat was Wrong!\n')
    else:
        print("No, that doesn't work.\n")

check_fermat(a, b, c, n)
