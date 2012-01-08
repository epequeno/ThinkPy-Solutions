# Two words are a "reverse pair" if each is the reverse of the other. Write
# a program that finds all the reverse pairs in the word list.

# Current Status: Complete

word_file = open('words.txt')

def make_list():
    list_ = []
    for word in word_file:
        list_.append(word.strip('\r\n'))
    return list_
    
word_list = make_list()

def make_dict():
    dict_ = {}
    for word in word_list:
        dict_[word] = None
    return dict_
    
word_dict = make_dict()

def find_rev_pairs():
    for word in word_list:
        if word[::-1] in word_dict:
            print word, word[::-1]

find_rev_pairs()