# Markov analysis:
# 1. Write a program to read a text from a file and perform Markov analysis. 
# The result should be a dictionary that maps from prefixes to a collection 
# of possible suffixes. The collection might be a list, tuple, or dictionary;
# it is up to you to make an appropriate choice. You can test your program 
# with prefix length two, but you should write the program in a way that 
# makes it easy to try other lengths.
# 2. Add a function to the previous program to generate random text based on 
# the Markov analysis.
# Here is an example from Emma with prefix length 2:
# He was very clever, be it sweetness or be angry, ashamed or only amused, at
# such a stroke. She had never thought of Hannah till you were never meant for
# me?" "I cannot make speeches, Emma:" he soon cut it all himself.
# For this example, I left the punctuation attached to the words. The result 
# is almost syntactically correct, but not quite. Semantically, it almost 
# makes sense, but not quite.
# What happens if you increase the prefix length? Does the random text make 
# more sense?
# 3. Once your program is working, you might want to try a mash-up: if you 
# analyze text from two or more books, the random text you generate will
# blend the vocabulary and phrases from the sources in interesting ways.

