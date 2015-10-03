# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list. Can you
# make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"

# Current Status: Incomplete

target = 'acefhlo'

with open('words.txt', 'r') as fd:
    word_list = fd.read().splitlines()


def uses_only(word, string):
    for letter in word:
        if letter not in string:
            return False
    return True


words = [word for word in word_list if uses_only(word, target)]
print "There are {} words that use only '{}', here's a sample: {}".format(len(words), target, words[:10])

# There are 188 words in the list that use only the letters found in 'acefhlo'
# so it's very likely to make a sentence with those words.