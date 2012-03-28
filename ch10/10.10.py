# Two words "interlock" if taking alternating letters from each forms a new 
# word.
# For example, "shoe" and "cold" interlock to form "schooled."
# 1. Write a program that finds all pairs of words that interlock. Hint: 
# don't enumerate all pairs!
# 2. Can you find any words that are three-way interlocked; that is, every 
# third letter forms a word, starting from the first, second or third?

# Current Status: Complete

word_list = [word.rstrip('\r\n') for word in open('words.txt', 'r')]

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
    word1 = word[i::3]
    word2 = word[i + 1::3]
    word3 = word[i + 2::3]
    return (word1, word2, word3)
    
def find_3way():
    answer = []
    for word in word_list:
        for i in range(0, 3):
            split_ = split_word2(word, i)
            if (split_[0] in word_dict and
                split_[1] in word_dict and
                split_[2] in word_dict):
                    answer.append((word,
                           split_[0],
                           split_[1],
                           split_[2]))
    return answer
                           
print find_3way()
print "Done"

#output
#[('abacuses', 'ace', 'bus', 'as'), ('abalone', 'ale', 'bo', 'an'),
# ('abalones', 'ale', 'bos', 'an'), ('abased', 'as', 'be', 'ad'),
# ('abaser', 'as', 'be',...