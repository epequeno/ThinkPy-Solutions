# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:08:41 2011

@author: steven
"""

# Rewrite this function so that instead of traversing the string, it uses the
# three-parameter version of find from the previous section.

# Current Status: Complete

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

def count(word, letter):
    count = 0
    index = 0
    while index < len(word):
        if find(word, letter, index) != -1:
            count += 1
        index = find(word, letter, index) + 1
    return count
    
print count("banana", "a")