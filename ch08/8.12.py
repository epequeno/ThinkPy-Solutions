# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 19:24:25 2011

@author: steven
"""

# ROT13 is a weak form of encryption that involves “rotating” each letter in a
# word by 13 places. To rotate a letter means to shift it through the alphabet,
# wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and
# ’Z’ shifted by 1 is ’A’. Write a function called rotate_word that takes a 
# string and an integer as parameters, and that returns a new string that 
# contains the letters from the original string “rotated” by the given amount.
# For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is 
# “cubed”. You might want to use the built-in functions ord, which converts a 
# character to a numeric code, and chr, which converts numeric codes to 
# characters.
# Potentially offensive jokes on the Internet are sometimes encoded in ROT13. 
# If you are not easily offended, find and decode some of them.

def rot13(word, amount):
    rotated = ''
    for letter in word:
        letter = ord(letter) + amount
        rotated = rotated + chr(letter)
    return rotated
    
print rot13("cheer", 7)