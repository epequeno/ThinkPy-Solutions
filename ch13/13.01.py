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
#
# Exercise 2  
# Go to Project Gutenberg (gutenberg.org) and download your favorite
# out-of-copyright book in plain text format.
#
# Modify your program from the previous exercise to read the book you
# downloaded, skip over the header information at the beginning of the file,
# and process the rest of the words as before.
#
# Then modify the program to count the total number of words in the book, and
# the number of times each word is used.
#
# Print the number of different words used in the book. Compare different
# books by different authors, written in different eras. Which author uses
# the most extensive vocabulary?
#
# Exercise 3   Modify the program from the previous exercise to print the 20
# most frequently-used words in the book.
# Exercise 4   Modify the previous program to read a word list
# (see Section 9.1) and then print all the words in the book that are not in
# the word list. How many of them are typos? How many of them are common words
# that should be in the word list, and how many of them are really obscure?

# Exercise 1
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

# Exercise 2
def words_sans_header():
    list_ = []
    signal = "*** START OF THIS"
    flag = False
    for line in open('origin.txt', 'r'):
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
            
print "The book has %s 'words'" % \
      len([clean(word) for word in words_sans_header()]), "sans header"
      
def histogram():
    hist = {}
    words_ = words_sans_header()
    for word in words_:
        hist[word] = hist.get(word, 0) + 1
    return hist
    
hist = histogram()
    
print "There are %s unique 'words'" % len(hist)

# Exercise 3
def top20():
    list_ = [(hist[k], k) for k in hist]
    list_.sort(reverse=True)
    print '\nThe top20 words are:'
    for i in range(0, 20):
        print '%s)' % (i + 1), '%s' % list_[i][1], '(%s)' % list_[i][0]
    
top20()

# Exercise 4
def set_sub():
    word_set = set(word.rstrip('\r\n') for word in open('words.txt', 'r'))
    book_set = set(clean(word) for word in words_sans_header())
    return list(book_set - word_set)
    
print set_sub()