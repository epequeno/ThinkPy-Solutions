# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:51:00 2011

@author: steven
"""

# Modify find so that it has a third parameter, the index in word where it 
# should start looking.

# Current Status: Complete

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print find("abddddddcd", "d", 8)

# in this example "d" is found several times in the string, the program is 
# set to exit when it finds the first occourance of the 'letter.' If we were 
# to start the search at index 2, "d" is found there, 2 is returned and the 
# program exits.  If we were to start at index 8 the program doesn't see a "d"
# at index 8, increments i to 9, finds "d" at index 9 and returns 9.