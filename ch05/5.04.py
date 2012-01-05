# The Koch curve is a fractal that looks something like this:
# To draw a Koch curve with length x, all you have to do is
# 1. Draw a Koch curve with length x/3.
# 2. Turn left 60 degrees.
# 3. Draw a Koch curve with length x/3.
# 4. Turn right 120 degrees.
# 5. Draw a Koch curve with length x/3.
# 6. Turn left 60 degrees.
# 7. Draw a Koch curve with length x/3.
# The only exception is if x is less than 3. In that case, you can just draw
# a straight line with length x.
# function called koch that takes a turtle and a length as parameters, and
# that uses the turtle to draw a Koch curve with the given length.
# 2. Write a function called snowflake that draws three Koch curves to make
# the outline of a snowflake.
# You can see my solution at thinkpython.com/code/koch.py.
# 3. The Koch curve can be generalized in several ways. 
# See wikipedia.org/wiki/Koch_snowflake for examples and implement your
# favorite.

# Current Status: Incomplete