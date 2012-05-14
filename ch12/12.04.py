# More anagrams!
# 1. Write a program that reads a word list from a file (see Section 9.1) 
# and prints all the sets of words that are anagrams.
# Here is an example of what the output might look like:
# ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
# ['retainers', 'ternaries']
# ['generating', 'greatening']
# ['resmelts', 'smelters', 'termless']
# Hint: you might want to build a dictionary that maps from a set of letters 
# to a list of words that can be spelled with those letters. The question is,
# how can you represent the set of letters in a way that can be used as a key?
# 2. Modify the previous program so that it prints the largest set of anagrams
# first, followed by the second largest set, and so on.
# 3. In Scrabble a "bingo" is when you play all seven tiles in your rack, along
# with a letter on the board, to form an eight-letter word. What set of 8 
# letters forms the most possible bingos? Answer: 'aeginrst'
# Hint: there are seven.
# 4. Two words form a "metathesis pair" if you can transform one into the other
# by swapping two letters; for example, "converse" and "conserve." Write a 
# program that finds all of the metathesis pairs in the dictionary. Hint: don't
# test all pairs of words, and don't test all possible swaps.
# You can download a solution from thinkpython.com/code/anagram_sets.py.

# Status: Complete

words_list = [line.strip('\r\n') for line in open('words.txt', 'r')]

def make_anagram_dict(mylist):
    '''Main grunt work. Returns dict which maps fingerprints to anagrams based 
    on that fingerprint. Iterates through the list of words once to create a 
    dict with the fingerprints. Iterates again to append matches to the 
    fingerprints dict. Finally, iterating through the dict to filter out 
    fingerprints that produced a list of length 1'''
    fingerprints = dict()
    for word in mylist:
        fp = ''.join(sorted(word))
        if fp not in fingerprints:
            fingerprints[fp] = []
        
        if fp in fingerprints:
            fingerprints[fp].append(word)
    
    filtered_dict = dict()
    for fp in fingerprints:
        if len(fingerprints[fp]) <= 1:
            pass
        else:
            filtered_dict[fp] = fingerprints[fp]

    return filtered_dict

words_dict = make_anagram_dict(words_list)

def print_anagrams(mydict):
    '''Uses a generator to call and print 5 items from mydict'''
    fp = (fp for fp in mydict)

    print "Sample from anagram dict:"
    i = 0
    while i < 5:
        fp_next = fp.next()
        print "%s) %s:" % ((i + 1), fp_next), mydict[fp_next]
        i += 1

    print "..."
    print "\n"


print_anagrams(words_dict)

def sort_anagrams(mydict):
    '''Returns a list of lists containing all anagram matches. The longest list
     (most anagrams) is at the top'''
    anagrams_lists = []
    for fp in mydict:
        anagrams_lists.append(mydict[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    for i in range(0, 5):
        print "%s)" % (i + 1), anagrams_lists[i]
    print "..."
    print "\n"


sort_anagrams(words_dict)

def find_bingos(mydict):
    '''Filters mydict for keys of length 8. Sorts a list of the values
     (lists) and sorts by length in reverse order'''
    candidates = [mydict[key] for key in mydict if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print "Top Bingos:"
    for i in range(0, 5):
        fp = ''.join(sorted(candidates[i][0]))
        print "%s) %s:" % ((i + 1), fp), candidates[i]

    print "..."
    print "\n"

find_bingos(words_dict)

def is_metathesis(reference, test):
    '''If two anagrams mismatch exactly twice they are metathesis pairs.
     Caution: This function assumes strings of equal length'''
    i = 0
    count = 0
    while i <= (len(reference) - 1):
        if reference[i] != test[i]:
            count += 1
        i += 1
    if count == 2:
        return True
    return False


def find_metathesis(mydict):
    '''mydict values are lists, we use index 0 as a reference and check the
     rest of the list (1 to end of list) against that reference word.'''
    answer = []
    for fp in mydict:
        reference = mydict[fp][0]
        for i in range(1, (len(mydict[fp]) - 1)):
            test = mydict[fp][i]
            if is_metathesis(reference, test):
                answer.append([reference, test])
    
    print "Sample of metathesis pairs:"
    for i in range(0, 5):
        print "%s)" % (i + 1), answer[i]
    print "..."

find_metathesis(words_dict)