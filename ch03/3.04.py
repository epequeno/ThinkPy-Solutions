# Current Status: Complete

# A function object is a value you can assign to a variable or pass as an 
# argument. For example, do_twice is a function that takes a function object 
# as an argument and calls it twice:
# 
# def do_twice(f):
#    f()
#    f()
#
# Here's an example that uses do_twice to call a function named print_spam 
# twice.
#
# def print_spam():
#    print 'spam'
# do_twice(print_spam)
#
# 1. Type this example into a script and test it.

def do_twice(f):
   f()
   f()

def print_spam():
   print 'spam'

do_twice(print_spam)

# 2. Modify do_twice so that it takes two arguments, a function object and
# a value, and calls the function twice, passing the value as an argument.

word = raw_input('What word to repeat?\n')

def do_twice(f, word):
   f(word)
   f(word)

def print_spam(word):
   print word

do_twice(print_spam, word)

# 3. Write a more general version of print_spam, called print_twice, that 
# takes a string as a parameter and prints it twice.

string = "steven"

def print_twice(string):
   print string
   print string

print_twice(string)


# 4. Use the modified version of do_twice to call print_twice twice, passing 
# 'spam' as an argument.

newWord = "spam"
do_twice(print_twice, newWord)


# 5. Define a new function called do_four that takes a function object and 
# a value and calls the function four times, passing the value as a parameter.
# There should be only two statements in the body of this function, not four.
# You can see my solution at thinkpython.com/code/do_four.py.