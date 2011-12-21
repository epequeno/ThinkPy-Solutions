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
# letters forms the most possible bingos?
# Hint: there are seven.
# 4. Two words form a "metathesis pair" if you can transform one into the other
# by swapping two letters; for example, "converse" and "conserve." Write a 
# program that finds all of the metathesis pairs in the dictionary. Hint: don't
# test all pairs of words, and don't test all possible swaps.
# You can download a solution from thinkpython.com/code/anagram_sets.py.

# Status: Incomplete

word_file = open('words.txt')
list_of_sorted_words = open('list_of_sorted_words.txt', 'w')

def create_list_of_sorted_words(word_list):
    '''Creates a file of each word in the word_file
    with each word's letters sorted by alpha. This will give
    us the group of words to test is_anagrams against'''
    sorted_list = []
    for word in word_list:
        sorted_word = sorted(word)
        sorted_word = ''.join(sorted_word)
        if sorted_word in sorted_list: # eliminate duplicates
            pass
        else:
            sorted_list.append(sorted_word)
            list_of_sorted_words.write(sorted_word)
    
#create_list_of_sorted_words(word_file)

def is_anagram(sorted_word, test_word):
    return sorted_word == sorted(test_word)