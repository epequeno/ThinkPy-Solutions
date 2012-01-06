# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list. Can you
# make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"

# Current Status: Incomplete

word_file = open('words.txt')

def make_list():
    word_list = []
    for word in word_file:
        word_list.append(word.rstrip('\r\n'))
    return word_list
    
word_list = make_list()

def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True
    
def make_sentence(list):
    count = 0
    for word in word_list:
        if uses_only(word, 'acefhlo'):
            print word
            count += 1
    return count

print make_sentence(word_list)

# There are 188 words in the list that use only the letters found in 'acefhlo'
# so it's very likely to make a sentence with those words. 