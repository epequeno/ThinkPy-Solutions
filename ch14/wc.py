# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 15:52:00 2011

@author: steven
"""

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count
    
if __name__ == '__main__':
    print linecount('wc.py')