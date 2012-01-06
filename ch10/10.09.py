# Two words are a "reverse pair" if each is the reverse of the other. Write
# a program that finds all the reverse pairs in the word list.

# Current Status: Incomplete

word_file = open('words.txt')

def make_list():
    word_list = []
    for word in word_file:
        word = word[:-2]
        word_list.append(word)
    return word_list
    
word_list = make_list()

def find_rev_pairs(word_list):
    results = []
    for word in word_list:
        if word[::-1] in word_list:
            results.append(word)
            word_list.remove(word[::-1])
    return results
            
print find_rev_pairs(word_list)