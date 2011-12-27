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

file_of_words = open('words.txt')
file_of_sorted_words = open('list_of_sorted_words.txt')

def make_word_list():
    word_list= []
    for word in file_of_words:
        word_list.append(word.strip('\n'))
    return word_list
    
word_list = make_word_list()

def make_sorted_word_list():
    sorted_word_list = []
    for sorted_word in file_of_sorted_words:
        sorted_word_list.append(sorted_word.strip('\n'))
    return sorted_word_list

sorted_word_list = make_sorted_word_list()

def is_anagram(sorted_word, test_word):
    return sorted(sorted_word) == sorted(test_word)
   
def make_dict():
    sorted_to_anagrams = {}
    for sorted_word in sorted_word_list:
        sorted_to_anagrams[sorted_word] = []
    return sorted_to_anagrams
    
sorted_to_anagrams = make_dict()

def match_sorted_word_to_anagram():
    for word in word_list:
        temp_word = sorted(word)
        temp_word = ''.join(temp_word)
        if temp_word in sorted_to_anagrams:
            sorted_to_anagrams[temp_word].append(word)
    final_dict = {}
    for key in sorted_to_anagrams:
        if len(sorted_to_anagrams[key]) > 1:
            final_dict[key] = sorted_to_anagrams[key]
    return final_dict
    
final_dict = match_sorted_word_to_anagram()

def make_sorted_list_of_anagrams():
    sorted_by_length_list = []
    for key in final_dict:
        sorted_by_length_list.append(final_dict[key])
    sorted_by_length_list.sort(key=len, reverse=True)
    return sorted_by_length_list
    
print make_sorted_list_of_anagrams()