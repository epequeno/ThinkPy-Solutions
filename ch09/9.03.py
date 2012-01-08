# Exercise 9.3
# Write a function named avoids that takes a word and a string of forbidden 
# letters, and that returns True if the word doesnt use any of the forbidden 
# letters.

# Current Status: Complete

word = str("steven")
string = str("qx")

def avoids(word, string):
    for letter in string:
        if letter in word:
            return False
    return True
    
print avoids(word, string)