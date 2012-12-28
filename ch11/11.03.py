# Dictionaries have a method called keys that returns the keys of the
# dictionary, in no particular order, as a list.
# Modify print_hist to print the keys and their values in alphabetical order.

# Current Status: Complete


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary


def print_hist(histogram):
    histoList = histogram.keys()
    histoList.sort()
    for letter in histoList:
        print letter, histogram[letter]

h = histogram('parrot')
print_hist(h)