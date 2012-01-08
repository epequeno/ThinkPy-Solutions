# Two words "interlock" if taking alternating letters from each forms a new 
# word.
# For example, "shoe" and "cold" interlock to form "schooled."
# 1. Write a program that finds all pairs of words that interlock. Hint: 
# don't enumerate all pairs!
# 2. Can you find any words that are three-way interlocked; that is, every 
# third letter forms a word, starting from the first, second or third?

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

def split_word(word):
    word1 = word[::2]
    word2 = word[1::2]
    return (word1, word2)
    
def find_interlocked():
    for word in word_list:
        if (split_word(word)[0] in word_dict and
            split_word(word)[1] in word_dict):
                print word, split_word(word)[0], split_word(word)[1]
                
# find_interlocked()

def split_word2(word, i):
    if i == 1:
        word1 = word[::3]
        word2 = word[1::3]
        word3 = word[2::3]
    elif i == 2:
        word1 = word[1::3]
        word2 = word[2::3]
        word3 = word[3::3]
    else:
        word1 = word[2::3]
        word2 = word[3::3]
        word3 = word[4::3]
    return (word1, word2, word3)
    
def find_3way():
    for word in word_list:
        for i in range(1, 4):
            if (split_word2(word, i)[0] in word_dict and
                split_word2(word, i)[1] in word_dict and
                split_word2(word, i)[2] in word_dict):
                    print (word,
                           split_word2(word, i)[0],
                           split_word2(word, i)[1],
                           split_word2(word, i)[2])
                           
find_3way()