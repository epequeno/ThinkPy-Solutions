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
    for p in prefixes:
        if p in ['O', 'Q']:
            yield '{}uack'.format(p)
        else:
            yield '{}ack'.format(p)

for i in list(ducks()):
    print i
