# 13.1  Word frequency analysis
# As usual, you should at least attempt the following exercises before you
# read my solutions.
#
# Exercise 1   Write a program that reads a file, breaks each line into words, 
# strips whitespace and punctuation from the words, and converts them to
# lowercase.
# Hint: The string module provides strings named whitespace, which contains
# space, tab, newline, etc., and punctuation which contains the punctuation
# characters. Let's see if we can make Python swear:
#
# >>> import string
# >>> print string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# Also, you might consider using the string methods strip, replace and
# translate.

from string import punctuation, whitespace

book = 'origin.txt'

with open(book, 'r') as fd:
    words = fd.read().split()

#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuation) or (char in whitespace)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print "{} has {} 'words'".format(book, len([clean(word) for word in words]))