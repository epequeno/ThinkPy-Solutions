# This is a rewrite of the palindrome test.  The goal is to take a variable
# string "word" and test if the first and last chars of the string are the same
# if they are then pass along the middle of the variable to get tested (n - 2).
# Repeat this until len(word) <= 2.  This handles three possible cases: 
#
# Case 1: word == "aa" | The two characters are the same (True for palindromes)
# Case 2: word == "ab" | The two characters are not the same (False)
# Case 3: word == "a"  | The single character is the center of the word (True)
#
# Any word that has first and last characters equal until cases 1 and 3 become 
# "True" is a palindrome. If case 2 comes up, the function should produce 
# "False".
#

word = str(raw_input('Want to see if it is a palindrome?\n'))

def is_palindrome(word):
   if len(word) <= 2 and word[0] == word[-1]:
       print 'True'
   elif word[0] == word[-1]:
       is_palindrome(word[1:-1])
   else:
       print 'False'

is_palindrome(word)
