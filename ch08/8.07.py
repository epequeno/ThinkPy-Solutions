# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:31:20 2011

@author: steven
"""

# There is a string method called count that is similar to the function in the
# previous exercise. Read the documentation of this method and write an 
# invocation that counts the number of a's in 'banana'.

# Current Status: Complete

word = "banana"
letter = "a"

def count(word, letter):
    return word.count("a")
    
print count(word, letter)