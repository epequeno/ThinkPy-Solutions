#Finding the words from the book that are not in the word list from words.txt
# is a problem you might recognize as set subtraction; that is, we want to find
# all the words from one set (the words in the book) that are not in another
# set (the words in the list).
#
#subtract takes dictionaries d1 and d2 and returns a new dictionary that
# contains all the keys from d1 that are not in d2. Since we don’t really care
# about the values, we set them all to None.
#
#def subtract(d1, d2):
#    res = dict()
#    for key in d1:
#        if key not in d2:
#            res[key] = None
#    return res
#To find the words in the book that are not in words.txt, we can use
# process_file to build a histogram for words.txt, and then subtract:
#words = process_file('words.txt')
#diff = subtract(hist, words)
#
#print "The words in the book that aren't in the word list are:"
#for word in diff.keys():
#    print word,
#Here are some of the results from Emma:
#The words in the book that aren't in the word list are:
# rencontre jane's blanche woodhouses disingenuousness 
#friend's venice apartment ...
#Some of these words are names and possessives. Others, like “rencontre,” are
# no longer in common use. But a few are common words that should really be in
# the list!
#Exercise 6  
#Python provides a data structure called set that provides many common set
# operations. Read the documentation at docs.python.org/lib/types-set.html 
# and write a program that uses set subtraction to find words in the book 
# that are not in the word list.
#
