#Exercise 3   Modify the program from the previous exercise to print the 20
# most frequently-used words in the book.

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

def histogram(data):
    hist = {}
    for word in data:
        hist[word] = hist.get(word, 0) + 1
    return hist

def stats():
    for book in books:
        print "Stats for %s:" % book.name
        data = [clean(word) for word in words(book)]
        print " Total: %s" % len(data)
        hist = histogram(data)
        print " Unique: %s" % len(hist)
        list_ = [(hist[k], k) for k in hist]
        list_.sort(reverse=True)
        print " The top20 were:"
        for i in range(0, 20):
            print " %s)" % (i + 1), list_[i][1]
stats()