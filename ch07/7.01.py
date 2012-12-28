# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 19:24:39 2011

@author: steven
"""

# Rewrite the function print_n from Section 5.8 using iteration instead of
# recursion.

# from 5.8:
#def print_n(s, n):
#    if n <= 0:
#        return
#    print s
#    print_n(s, n-1)

# Current Status: Complete


def print_n(s, n):
    i = 0
    while i < n:
        print s
        i += 1

print_n('steven', 10)