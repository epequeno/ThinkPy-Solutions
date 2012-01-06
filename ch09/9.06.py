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

def find_abecedarian(list):
    word_count = 0
    for word in list:
        if word == ''.join(sorted(word)):
            print word
            word_count += 1
    print word_count
            
find_abecedarian(word_list)