# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters
# at least once. How many words are there that use all the vowels aeiou? How 
# about aeiouy?

# Current Status: Complete

word_file = open('words.txt')

def make_list():
    final_list = []
    for word in word_file:
        final_list.append(word.strip('\r\n'))
    return final_list
    
word_list = make_list()

def uses_all(word, string):
    count = 0
    for letter in string:
        if letter in word:
            count += 1
    if count == len(string):
        return True
    else:
        return False
        
def find_uses_all_vowels(list):
    count = 0
    string = 'aeiouy'
    for word in list:
        if uses_all(word, string):
            count += 1
    return count
    
print find_uses_all_vowels(word_list)

# There are 598 words that use the 5 normal vowels and only 42 that use those
# and y