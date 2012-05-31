#Exercise 3   Modify the program from the previous exercise to print the 20
# most frequently-used words in the book.

#TODO: fix rest of file to work with new origin aliases

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [space for space in string.whitespace]

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

books = [origin, huck, frank, great, meta, sherlock, tale]

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    op = open(book, 'r')
    for line in op:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    op.close()
    return list_
  
myList = words(origin)

# def clean(word):
#     result = ''
#     for char in word:
#         if (char in whitespaces) or (char in punctuations):
#             pass
#         else:
#             result += char.lower()
#     return result

# def histogram(data):
#     hist = {}
#     for word in data:
#         hist[word] = hist.get(word, 0) + 1
#     return hist

# def stats():
#     for book in books:
#         print "Stats for %s:" % book.name
#         data = [clean(word) for word in words(book)]
#         print " Total: %s" % len(data)
#         hist = histogram(data)
#         print " Unique: %s" % len(hist)
#         list_ = [(hist[k], k) for k in hist]
#         list_.sort(reverse=True)
#         print " The top20 were:"
#         for i in range(0, 20):
#             print " %s)" % (i + 1), list_[i][1]
# stats()