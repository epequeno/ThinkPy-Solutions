# Write a program that reads a file, breaks each line into words, strips
# whitespace and punctuation from the words, and converts them to lowercase.
# Hint: The string module provides strings named whitespace, which contains
# space, tab, newline, etc., and punctuation which contains the punctuation
# characters. Let's see if we can make Python swear:
# >>> import string
# >>> print string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# Also, you might consider using the string methods strip, replace and 
# translate.

# Current Status: Complete

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]

data = open('origin.txt', 'r')

#split into words
def words():
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
        
print [clean(word) for word in words()]