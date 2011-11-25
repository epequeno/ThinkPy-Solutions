# Write a function called most_frequent that takes a string and prints the 
# letters in decreasing order of frequency. Find text samples from several
# different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at 
# wikipedia.org/wiki/Letter_frequencies.

text = 'The rain in Spain falls mainly on the plains!!!!'

def make_list(x):
    new_list = []
    for letter in x:
        if not letter.isalpha():
            pass
        else:
            new_list.append(letter.lower())
    return new_list

def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary
    
def most_frequent(text):
    dictionary = make_list(text)
    dictionary = make_dict(dictionary)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print letter, count
    
most_frequent(text)