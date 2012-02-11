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

file_of_words = open('words.txt')
file_of_sorted_words = open('list_of_sorted_words.txt')

word_list = [word.rstrip('\n') for word in file_of_words]
sorted_word_list = [word.rstrip('\n') for word in file_of_sorted_words]

def make_dict():
    '''Create dictionary that masp from sorted words to empty lists '''
    sorted_to_anagrams = {}
    for sorted_word in sorted_word_list:
        sorted_to_anagrams[sorted_word] = []
    return sorted_to_anagrams
    
sorted_to_anagrams = make_dict()

def match_sorted_word_to_anagram():
    '''Checks if a sorted word from the word_list is already in the dictionary
    if so, append the unsorted word to the list (value) for the key (sorted
    word). Returns only words which have at least 1 anagram (>= 2 words in 
    a list)'''
    for word in word_list:
        temp_word = ''.join(sorted(word))
        if temp_word in sorted_to_anagrams:
            sorted_to_anagrams[temp_word].append(word)
    final_dict = {}
    for key in sorted_to_anagrams:
        if len(sorted_to_anagrams[key]) > 1:
            final_dict[key] = sorted_to_anagrams[key]
    return final_dict
    
final_dict = match_sorted_word_to_anagram()

def make_sorted_list_of_anagrams():
    '''Make a list of lists of anagrams sorted by length in reverse order'''
    sorted_by_length_list = []
    for key in final_dict:
        sorted_by_length_list.append(final_dict[key])
    sorted_by_length_list.sort(key=len, reverse=True)
    return sorted_by_length_list
    
def find_bingos():
    ''' Find and return the longest list of anagrams whose word length=8'''
    bingos = []
    for key in final_dict:
        if len(key) == 8:
            bingos.append(final_dict[key])
    bingos.sort(key=len, reverse=True)
    return bingos[0]
    
#print find_bingos()

sorted_list_of_anagrams = make_sorted_list_of_anagrams()

def is_metathesis(reference_word, test_word):
    '''Steps though reference_word and test_word and counts how often the 
    two words differ. Metathesis pairs will mismatch exactly twice'''
    mismatch_count = 0
    i = 0
    while i <= len(reference_word) - 1:
        if reference_word[i] != test_word[i]:
            mismatch_count += 1
        i += 1
    if mismatch_count == 2:
        return True
    else:
        return False

def find_metathesis_pairs():
    '''For each list of anagrams produced by make_sorted_list_of_anagrams, 
    use the first element as a reference word and check the rest of the 
    list against that reference word using is_metathesis. Print pairs of 
    words found to be metathesis pairs'''
    for test_list in sorted_list_of_anagrams:
        reference_word = test_list[0]
        i = 1
        while i <= len(test_list) - 1:
            if is_metathesis(reference_word, test_list[i]):
                print reference_word, test_list[i]
            i += 1

find_metathesis_pairs()