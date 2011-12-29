# Here's another Car Talk Puzzler:
# What is the longest English word, that remains a valid English word, as you
# remove its letters one at a time?
# Now, letters can be removed from either end, or the middle, but you can't
# rearrange any of the letters. Every time you drop a letter, you wind up with 
# another English word. If you do that, you're eventually going to wind up with
# one letter and that too is going to be an English word-one that's found in 
# the dictionary. I want to know what's the longest word and how many letters
# does it have?
# I'm going to give you a little modest example: Sprite. Ok? You start off with
# sprite, you take a letter off, one from the interior of the word, take the r
# away, and we're left with the word spite, then we take the e off the end, 
# we're left with spit, we take the s off, we're left with pit, it, and I.
# Write a program to find all words that can be reduced in this way, and then 
# find the longest one.
# This exercise is a little more challenging than most, so here are some 
# suggestions:
# 1. You might want to write a function that takes a word and computes a list
# of all the words that can be formed by removing one letter. These are the 
# "children" of the word. 
# 2. Recursively, a word is reducible if any of its children are reducible. As
# a base case, you can consider the empty string reducible.
# 3. The wordlist I provided, words.txt, doesn't contain single letter words.
# So you might want to add "I", "a", and the empty string.
# 4. To improve the performance of your program, you might want to memoize 
# the words that are known to be reducible.
# You can see my solution at thinkpython.com/code/reducible.py.

# Current Status: Incomplete

word_file = open('words.txt')

def make_word_list():
    word_list = []
    for word in word_file:
        word_list.append(word.strip('\n'))
    word_list.append('a')
    word_list.append('i')
    word_list.sort(key=len, reverse=True)
    return word_list

word_list = make_word_list()

def create_map_of_children():
    word_dict = {}
    for word in word_list:
        word_dict[word] = []
    for word in word_list:
        i = 0
        while i <= len(word) - 1:
            if word.replace(word[i], '') in word_dict:
                word_dict[word].append(word.replace(word[i], ''))
                i += 1
            else:
                i += 1
    final_dict = {}
    for key in word_dict:
        if len(word_dict[key]) != 0:
            final_dict[key] = word_dict[key]
    return final_dict
    
map_of_children = create_map_of_children()

print map_of_children