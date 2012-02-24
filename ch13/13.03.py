#13.3  Word histogram
#
#Here is a program that reads a file and builds a histogram of the words in 
#the file:
#
#import string
#
#def process_file(filename):
#    h = dict()
#    fp = open(filename)
#    for line in fp:
#        process_line(line, h)
#    return h
#
#def process_line(line, h):
#    line = line.replace('-', ' ')
#    
#    for word in line.split():
#        word = word.strip(string.punctuation + string.whitespace)
#        word = word.lower()
#
#        h[word] = h.get(word, 0) + 1
#
#hist = process_file('emma.txt')
#This program reads emma.txt, which contains the text of Emma by Jane Austen.
#
#process_file loops through the lines of the file, passing them one at a time
# to process_line. The histogram h is being used as an accumulator.
#
#
#process_line uses the string method replace to replace hyphens with spaces
# before using split to break the line into a list of strings. It traverses
# the list of words and uses strip and lower to remove punctuation and convert
# to lower case. (It is a shorthand to say that strings are "converted;" 
# remember that string are immutable, so methods like strip and lower return
# new strings.)
#
#Finally, process_line updates the histogram by creating a new item or 
#incrementing an existing one.
#
#
#To count the total number of words in the file, we can add up the
# frequencies in the histogram:
#
#def total_words(h):
#    return sum(h.values())
#The number of different words is just the number of items in the dictionary:
#def different_words(h):
#    return len(h)
#Here is some code to print the results:
#print 'Total number of words:', total_words(hist)
#print 'Number of different words:', different_words(hist)
#And the results:
#Total number of words: 161073
#Number of different words: 7212