#13.4  Most common words
#
#To find the most common words, we can apply the DSU pattern; most_common
# takes a histogram and returns a list of word-frequency tuples, sorted in
# reverse order by frequency:
#
#def most_common(h):
#    t = []
#    for key, value in h.items():
#        t.append((value, key))
#
#    t.sort(reverse=True)
#    return t
#Here is a loop that prints the ten most common words:
#t = most_common(hist)
#print 'The most common words are:'
#for freq, word in t[0:10]:
#    print word, '\t', freq
#And here are the results from Emma:
#The most common words are:
#to      5242
#the     5204
#and     4897
#of      4293
#i       3191
#a       3130
#it      2529
#her     2483
#was     2400
#she     2364