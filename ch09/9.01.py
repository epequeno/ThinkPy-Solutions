# Write a program that reads words.txt and prints only the words with
# more than 20 characters (not counting whitespace).

# Current Status: Complete

with open('words.txt', 'r') as fd:
    wordList = fd.read().split()

print [word for word in wordList if len(word) > 20]