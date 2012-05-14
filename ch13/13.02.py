# -*- coding: utf-8 -*-
#Go to Project Gutenberg (gutenberg.org) and download your favorite 
#out-of-copyright book in plain text format.
#
#
#Modify your program from the previous exercise to read the book you 
#downloaded, skip over the header information at the beginning of the 
#file, and process the rest of the words as before.
#
#Then modify the program to count the total number of words in the book,
# and the number of times each word is used.
#
#
#Print the number of different words used in the book. Compare different 
#books by different authors, written in different eras. Which author uses 
#the most extensive vocabulary?

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

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
    for letter in word:
        if (letter in whitespaces) or (letter in punctuations):
            pass
        else:
            result += letter.lower()
    return result

def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

books = [origin, huck, frank, great, meta, sherlock, tale]

def stats():
    for book in books:
        book = open(book, 'r')
        print "Stats for %s:" % book.name
        data = [clean(word) for word in words(book)]
        book.close()
        print "  Total: %s" % len(data)
        print "  Unique: %s" % len(histogram(data))
                
stats()