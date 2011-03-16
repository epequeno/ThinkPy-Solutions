# Exercise 9.3
# Write a function named avoids that takes a word and a string of forbidden 
# letters, and that returns True if the word doesnt use any of the forbidden 
# letters.

word = str("steven")
string = str("q")

def avoids(word, string):
   if string in word:
       return
   else:
       print "True"

avoids(word, string)
