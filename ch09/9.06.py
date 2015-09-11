# Write a function called is_abecedarian that returns True if the letters
# in a word appear in alphabetical order (double letters are ok). How many
# abecedarian words are there?

# Current Status: Complete

with open('words.txt', 'r') as fd:
    word_list = fd.read().split()


def is_abecedarian(word):
    return word == ''.join(sorted(word))

print ("There are %s abecedarian words."
       % len([word for word in word_list if is_abecedarian(word)]))