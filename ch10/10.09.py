# Two words are a "reverse pair" if each is the reverse of the other. Write
# a program that finds all the reverse pairs in the word list.

# Current Status: Complete

with open('words.txt') as fd:
    word_list = fd.read().splitlines()

word_dict = {word: None for word in word_list}

def find_rev_pairs(word_dict):
    for word in word_dict:
        if word[::-1] in word_dict:
            print word, word[::-1]

find_rev_pairs(word_dict)