#Modify the previous program to read a word list (see Section 9.1) and then
# print all the words in the book that are not in the word list. How many of
# them are typos? How many of them are common words that should be in the word
# list, and how many of them are really obscure?

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [space for space in string.whitespace]

origin = open('origin.txt', 'r')
huck = open('huck.txt', 'r')
frank = open('frank.txt', 'r')
great = open('great.txt', 'r')
meta = open('meta.txt', 'r')
sherlock = open('sherlock.txt', 'r')
tale = open('tale.txt', 'r')

books = [origin, huck, frank, great, meta, sherlock, tale]

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for char in word:
        if (char in whitespaces) or (char in punctuations):
            pass
        else:
            result += char.lower()
    return result

