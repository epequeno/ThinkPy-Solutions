# Write a function that reads the file words.txt and builds a list with one 
# element per word. Write two versions of this function, one using the 
# append method and the other using the idiom t = t + [x]. Which one takes
# longer to run? Why?
# You can see my solution at thinkpython.com/code/wordlist.py.
#
word = open('words.txt')
wordList = [word.read()]

print wordList
