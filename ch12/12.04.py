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

with open('words.txt', 'r') as fd:
    words = fd.read().splitlines()

def make_anagram_dict(word_list):
    '''Take a list of words, return a dict with a fingerprint as the key
    and the anagrams made from that fingerprint as the value.'''
    anagrams = dict()
    for word in word_list:
        fp = ''.join(sorted(word))
        anagrams[fp] = anagrams.get(fp, [])
        anagrams[fp].append(word)

    anagrams = {fp: anagrams[fp] for fp in anagrams if len(anagrams[fp]) > 1}
    return anagrams

anagrams = make_anagram_dict(words)

def print_anagrams(anagrams):
    '''Uses a generator to call and print 5 items from mydict'''
    fp = (fp for fp in anagrams)

    print "Sample from anagram dict:"
    for i in range(1, 6):
        # call once, print twice
        fp_next = fp.next()
        print "%s) %s:" % (i, fp_next), anagrams[fp_next]

    print "..."
    print "\n"


print_anagrams(anagrams)


def sort_anagrams(anagrams):
    '''Returns a list of lists containing all anagram matches. The longest list
     (most anagrams) is at the top'''
    anagrams_lists = []
    for fp in anagrams:
        anagrams_lists.append(anagrams[fp])
    anagrams_lists.sort(key=len, reverse=True)

    print "Most anagrams:"
    for i in range(0, 5):
        print "%s) %d" % ((i + 1), len(anagrams_lists[i])), anagrams_lists[i]
    print "..."
    print "\n"


sort_anagrams(anagrams)


def find_bingos(anagrams):
    '''Filters mydict for keys of length 8. Sorts a list of the values
     (lists) and sorts by length in reverse order'''
    candidates = [anagrams[key] for key in anagrams if len(key) == 8]
    candidates.sort(key=len, reverse=True)

    print "Top Bingos:"
    for i in range(0, 5):
        fp = ''.join(sorted(candidates[i][0]))
        print "%s) %d: %s" % ((i + 1), len(candidates[i]), fp), candidates[i]

    print "..."
    print "\n"

find_bingos(anagrams)


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


def find_metathesis(anagrams):
    '''mydict values are lists, we use index 0 as a reference and check the
     rest of the list (1 to end of list) against that reference word.'''
    answer = []
    for fp in anagrams:
        reference = anagrams[fp][0]
        for i in range(1, (len(anagrams[fp]) - 1)):
            test = anagrams[fp][i]
            if is_metathesis(reference, test):
                answer.append([reference, test])

    print "Sample of metathesis pairs:"
    for i in range(0, 5):
        print "%s)" % (i + 1), answer[i]
    print "..."

find_metathesis(anagrams)