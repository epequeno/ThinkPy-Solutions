# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:36:45 2011

@author: steven
"""

# A string slice can take a third index that specifies the “step size;” that
# is, the number of spaces between successive characters. A step size of 2
#  means every other character; 3 means every third, etc.
# >>> fruit = 'banana'
# >>> fruit[0:5:2]
# 'bnn'
# A step size of -1 goes through the word backwards, so the slice [::-1] 
# generates a reversed string.
# Use this idiom to write a one-line version of is_palindrome from 
# Exercise 6.6.


#from 6.6:
#def is_palindrome(word):
#   if len(word) <= 2 and word[0] == word[-1]:
#       print 'True'
#   elif word[0] == word[-1]:
#       is_palindrome(word[1:-1])
#   else:
#       print 'False'

# Current Status: Complete

def is_palindrome(word):
    return word == word[::-1]

print is_palindrome("abcba")
print is_palindrome("steven")