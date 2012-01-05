# Current Status: Complete

# If you type an integer with a leading zero, you might get a confusing
# error:
# >>> zipcode = 02492
#                  ^
# SyntaxError: invalid token
# Other numbers seem to work, but the results are bizarre:
# >>> zipcode = 02132
# >>> print zipcode
# 1114
# Can you figure out what is going on? Hint: print the values 01, 010,
# 0100 and 01000.

# Solution: When you give the print statement something that doesn't start
# with a 0 it prints it faithfully

print 123

# But when you start the argument off with a 0 python assumes the value is 
# octal.  In this case if the binary input is 8 for example, the output
# is 010, the octal representation of binary 8.

print 010

# With this in mind, the problems with the zip code example are clear, octal
# only uses digits up to and including 7, starting off with a 0 (oct) then 
# passing along a 9 gives you the Syntax error.
# http://en.wikipedia.org/wiki/Octal