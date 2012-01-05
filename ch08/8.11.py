# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:42:49 2011

@author: steven
"""
# Current Status: Complete


# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each function,
# describe what the function actually does (assuming that the parameter is a
# string).

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
#
# This function will terminate too soon and provide a wrong answer. In the case
# of "Test" the first "T" would make c.islower() False and the program would 
# return False which isn't what we were looking for, there are indeed lowercase
# letters in the string but we were given "False" as the answer.  This tests
# whether the first letter in a string is lowercase since it will exit with
# True or False after the first letter no matter what the case. 

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

# In this case we can already know the answer will ALWAYS be "True."  This asks
# python to tell us if the string 'c' is lowercase regardless of what the 
# string itself contains.  For example if the string was 'STEVEN' it would 
# start with 'S' (since that is the first c in s), ignore that is is an 'S' and
# test if 'c' is lowercase, which it is. Telling us that there are lowercase 
# letters in the string when clearly there are not.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

# Getting closer to what we were asking for but still off a bit. In the case of
# "tesT" this would set 'flag' to True for "t", "e", and "s" which is what we 
# are looking for. But when it gets tot the final letter "T" 'flag' gets set to
# False which implies that there were no lowercase letters in the string, which
# is not true. This function tests whether the last letter in the string is 
# lowercase or not.

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
    
# This function performs as expected. 'flag' is set to False by default and it 
# will remain False for every c in s that fails c.islower(). The first time 
# that comes across a lowercase letter the condition 'flag' becomes:
# False or True which results in 'flag' being set to True. Once 'flag' is 
# reassigned, no lower- or uppercase letter can change 'flag' back to False.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
        
# This gets things a bit backwards and tests whether is word is ALL lowercase 
# or not. In the case of "tesT," "t," "e," and "s" pass the check, but "T"
# meets the condition that 'not c.islower("T")' is True, returning a False. 

print any_lowercase1("Test")
print any_lowercase2("STEVEN")
print any_lowercase3("tesT")
print any_lowercase4("tEST")
print any_lowercase5("tesT")