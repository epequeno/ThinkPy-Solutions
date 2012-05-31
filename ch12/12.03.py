# Write a function called most_frequent that takes a string and prints the 
# letters in decreasing order of frequency. Find text samples from several
# different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at 
# wikipedia.org/wiki/Letter_frequencies.

# Current Status: Complete

text = 'The rain in Spain falls mainly on the plains!!!!'

def make_dict(x):
    dictionary = {}
    for letter in x:
        dictionary[letter] = 1 + dictionary.get(letter, 0)
    return dictionary
    
def most_frequent(text):
    letters = [letter.lower() for letter in text if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print letter, count
    

most_frequent(text)