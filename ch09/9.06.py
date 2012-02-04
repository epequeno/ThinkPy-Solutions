# Write a function called is_abecedarian that returns True if the letters 
# in a word appear in alphabetical order (double letters are ok). How many
# abecedarian words are there?

# Current Status: Complete

word_file = open('words.txt')
word_list = [word.rstrip('\r\n') for word in word_file]

def is_abecedarian(word):
    return word == ''.join(sorted(word))

print ("There are %s abecedarian words." 
       % len([word for word in word_list if is_abecedarian(word)]))