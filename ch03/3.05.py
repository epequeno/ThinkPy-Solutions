# This exercise can be done using only the statements and other features we 
# have learned so far.
#
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
#
# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so 
# the value printed next appears on the same line.
# print '+',
# print '-'
# The output of these statements is '+ -'.
# A print statement all by itself ends the current line and goes to the next in
# line.
# 2. Use the previous function to draw a similar grid with four rows and four
# columns. You can see my solution at thinkpython.com/code/grid.py.

def print_border():
   print "+", "- " * 4, "+"

def print_row():
   row = "|", " " * 8, "|\n"
   print row * 4

def block():
   print_border()
   print_row()
   
block()
