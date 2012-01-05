# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 17:41:52 2011

@author: steven
"""

# Modify the program to fix this error.

# Current Status: Complete

prefixes = 'JKLMNOPQ'
suffix = 'ack'

def ducks():
    for i in prefixes:
        if i == "O" or i == "Q":
            print i + "u" + suffix
        else:
            print i + suffix

ducks()