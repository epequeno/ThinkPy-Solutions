# This exercise is a cautionary tale about one of the most common, and
# difficult to find, errors in Python.
# 1. Write a definition for a class named Kangaroo with the following methods:
# (a) An __init__ method that initializes an attribute named pouch_contents
# to an empty list.
# (b) A method named put_in_pouch that takes an object of any type and adds
# it to pouch_contents.
# (c) A __str__ method that returns a string representation of the Kangaroo
# object and the contents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to variables
# named kanga and roo, and then adding roo to the contents of kanga’s pouch.
# 2. Download thinkpython.com/code/BadKangaroo.py. It contains a solution to
# the previous problem with one big, nasty bug. Find and fix the bug.
# If you get stuck, you can download thinkpython.com/code/GoodKangaroo.py,
# which explains the problem and demonstrates a solution.

# Current Status: Complete

class Kangaroo(object):
    def __init__(self):
        self.pouch_contents = []
    
    def put_in_pouch(self, thing):
        self.pouch_contents.append(thing)
    
    def __str__(self):
        return "I have {} in my pouch".format(self.pouch_contents)
    
    def __repr__(self):
        return 'Kangaroo <{}>'.format(self.pouch_contents)