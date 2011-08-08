# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:34:55 2011

@author: steven
"""

# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

def string_backwards(string):
    """ Prints each letter of the given string, backwards, one letter per
    line """
    i = len(string)
    while i > 0:
        print string[i - 1]
        i -= 1

string_backwards("steven")