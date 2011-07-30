# Dictionaries have a method called get that takes a key and a default
# value. If the key appears in the dictionary, get returns the 
# corresponding value; otherwise it returns the default value.
# For example:
# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0
# Use get to write histogram more concisely. You should be able to 
# eliminate the if statement

def histogram(word):
    dictionary =  dict()
    for character in word:
        dictionary[character] = 1 + dictionary.get(character, 0)
    return dictionary
    
print histogram('antidisestablishmentarianism')

# http://en.wikibooks.org/wiki/Think_Python/Answers#Exercise_11.2