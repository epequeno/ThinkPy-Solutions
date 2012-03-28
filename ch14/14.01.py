#!/usr/bin/python

# Modify walk so that instead of printing the names of the files, it returns
# a list of names.

# Current Status: Complete


import os

cwd = os.getcwd()
names = []

def walk(directory):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            names.append(path)
        else:
            walk(path)
    print names

walk(cwd)

# Not exactly sure what the book wanted. Having a list of all the full paths
# is kind of ugly but the question calls what is printed 'names' so it was a 
# small modification to append the 'names' to a list. That was probably what
# was expected.

# output
# ['/home/steven/ThinkPy-Solutions/ch14/14.05.py',
#   '/home/steven/ThinkPy-Solutions/ch14/14.07.py',
#   '/home/steven/ThinkPy-Solutions/ch14/14.01.py',
#   '/home/steven/ThinkPy-Solutions/ch14/14.03.py',
#   '/home/steven/ThinkPy-Solutions/ch14/wc.py',
#   '/home/steven/ThinkPy-Solutions/ch14/14.06.py',
#   '/home/steven/ThinkPy-Solutions/ch14/14.04.py', 
#   '/home/steven/ThinkPy-Solutions/ch14/14.02.py']