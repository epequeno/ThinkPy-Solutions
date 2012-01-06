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