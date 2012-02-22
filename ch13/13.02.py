# Go to Project Gutenberg (gutenberg.net) and download your favorite 
# out-of-copyright book in plain text format.
# Modify your program from the previous exercise to read the book you 
# downloaded, skip over the header information at the beginning of the file, 
# and process the rest of the words as before.
# Then modify the program to count the total number of words in the book, and
# the number of times each word is used.
# Print the number of different words used in the book. Compare different
# books by different authors, written in different eras. Which author uses 
# the most extensive vocabulary?

# Current Status: Incomplete

import string

punctuations = [mark for mark in string.punctuation]
whitespaces = [char for char in string.whitespace]

data = open('origin.txt', 'r')

#split into words
def words():
    main = []
    line_count = 1
    for line in data:
        if line_count <= 20:
            line_count += 1
            pass
        else:
            for item in line.split():
                main.append(item)
    return main    
    
#remove punctuation, whitespace, uppercase
def clean(word):
    cleansed = ''
    for char in word:
        if ((char in punctuations) or (char in whitespaces)):
            pass
        else:
            cleansed += char.lower()
    return cleansed
        
clean_list = [clean(word) for word in words()]

print 'There are %s "words" in the book.' % len(clean_list)


def histogram():
    hist = {}
    for word in clean_list:
        if word not in hist:
            hist[word] = hist.get(word, 0) + 1
        else: hist[word] += 1
    return hist
    
def find_most_used():
    hist = histogram()
    list_ = []
    for key in hist:
        list_.append((hist[key], key))
    list_.sort(reverse=True)
    return list_
    
most_used = find_most_used()

def stats():
    x = 1
    while x <= 10:
        print "%s.)" % x, "%s" % most_used[x][1], "(%s)" % most_used[x][0], \
               "%.3f" % (most_used[x][0] / float(len(clean_list))), \
               "% of total"
        x += 1
        
print "The 10 most used words were:"
stats()