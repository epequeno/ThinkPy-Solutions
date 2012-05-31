# Two words are "rotate pairs" if you can rotate one of them and get the 
# other (see rotate_word in Exercise 8.12).
# Write a program that reads a wordlist and finds all the rotate pairs.

# Current Status: Incomplete

import rotate

word_file = open("words.txt")

def make_dict():
    dict_ = {}
    for word in word_file:
        dict_[word.strip('\r\n')] = None
    word_file.close()
    return dict_
    
word_dict = make_dict()

def find_rot_pairs():
    final_list = []
    for word in word_dict:
        for i in range(1, 26):
            if rotate.rotate_word(word, i) in word_dict:
                final_list.append((word, i, rotate.rotate_word(word, i)))
    final_list.sort()
    for pair in final_list:
        print pair

find_rot_pairs()