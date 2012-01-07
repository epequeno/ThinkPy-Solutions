# Write a function called is_abecedarian that returns True if the letters 
# in a word appear in alphabetical order (double letters are ok). How many
# abecedarian words are there?

# Current Status: Complete

word_file = open('words.txt')

def make_list():
    word_list = []
    for word in word_file:
        word_list.append(word.rstrip('\r\n'))
    return word_list
    
word_list = make_list()

def is_abecedarian(word):
    return word == ''.join(sorted(word))

def count_words():
    count = 0
    for word in word_list:
        if is_abecedarian(word):
            count += 1
    return count
    
print count_words()