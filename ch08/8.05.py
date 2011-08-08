# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:04:28 2011

@author: steven
"""

# Encapsulate this code in a function named count, and generalize it so that it
# accepts the string and the letter as arguments.

word = 'banana'
target = 'a'

def count(word, target):
    count = 0
    for letter in word:
        if letter == target:
            count += 1
    return count

print count(word, target)