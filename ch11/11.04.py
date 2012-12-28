# Modify reverse_lookup so that it builds and returns a list of all keys
# that map to v, or an empty list if there are none.

# Current Status: Complete


def reverse_lookup(dictionary, value):
    results = []
    for key in dictionary:
        if dictionary[key] == value:
            results.append(key)
    return results


def histogram(word):
    dictionary = dict()
    for letter in word:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary

h = histogram('parrot')
k = reverse_lookup(h, 2)
print k