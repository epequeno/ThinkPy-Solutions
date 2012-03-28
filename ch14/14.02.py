#!/usr/bin/python

# The os module provides a function called walk that is similar to this one
# but more versatile. Read the documentation and use it to print the names
# of the files in a given directory and its subdirectories.

# Current Status: Complete

import os

cwd = os.getcwd()

for one, two, three in os.walk(cwd):
    print one, three
    
# os.walk returns a 3-tuple with the directory path, names of subdirs as a list
# and finally the file names as a list also. 
# http://docs.python.org/library/os.html#os.walk

# output
# /home/steven/ThinkPy-Solutions/ch14 ['14.05.py', '14.07.py', '14.01.py', 
#                                      '14.03.py', 'wc.py', '14.06.py',
#                                      '14.04.py', '14.02.py']
