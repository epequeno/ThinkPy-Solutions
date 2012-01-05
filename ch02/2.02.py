# Current Status: Complete

# Type the following statements in the Python interpreter to see what they do:
# 5
# x = 5
# x + 1
# Now put the same statements into a script and run it. What is the output?
# Modify the script by transforming each expression into a print statement
# and then run it again.

print 5
print x = 5
print x + 1

# In the interpreter these lines do what you might intuitively expect.  '5'
# echoes 5, 'x = 5' assigns 5 to the variable x, 'x + 1' adds 1 to x where x 
# is 5 and echoes 6.

# If you put them directly into a script as is the script will do nothing,
# possibly assign 5 to x but then dump them once the script is done running.

# If you add the print statements you get a syntax error because when you ask 
# python to print x it doesn't understand what you mean when you then ask it
# to assign 5 to x, print or assign? What if the variable has changed? Do you 
# want the old variable or the new one printed?


# If the goal is to print 6 then you would do the variable assignment then 
# tell python to print the value of 5 with 1 added to it. In this case 
# python understands that x is 5, will stay 5 but 5 + 1 is what should be 
# printed.

# If the goal is to print each statment literally then you would need to 
# encapsulate each one with quotes like this:

print '5'
print 'x = 5'
print 'x + 1'
# would want to make the 
# variable assignment then print 
