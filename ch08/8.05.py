# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:04:28 2011

@author: steven
"""

# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.

# Current Status: Complete

myword = 'banana'
mytarget = 'a'


def count(word, target):
    i = 0
    for letter in word:
        if letter == target:
            i += 1
    return i

print count(myword, mytarget)