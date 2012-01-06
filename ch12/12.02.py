# In this example, ties are broken by comparing words, so words with the same 
# length appear in alphabetical order. For other applications you might want 
# to break ties at random. Modify this example so that words with the same 
# length appear in random order. Hint: see the random function in the random
# module.

# Current Status: Incomplete

import random

words = open('words.txt')

def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))
        t.sort(reverse=True)
    res = []
    for length, word in t:
        res.append(word)
    return res

print sort_by_length(words)