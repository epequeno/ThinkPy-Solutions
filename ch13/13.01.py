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

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]

#split into words
def words():
    data = open('origin.txt', 'r')
    main = []
    for line in data:
        for item in line.split():
            main.append(item)
    return main
    data.close()

#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuations) or (char in whitespaces)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
print "The book has %s 'words'" % len([clean(word) for word in words()])