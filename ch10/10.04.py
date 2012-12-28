# Two words are anagrams if you can rearrange the letters from one to spell
# the other. Write a function called is_anagram that takes two strings and
# returns True if they are anagrams.

# Current Status: Complete

stringOne = "events"
stringTwo = "steven"


def is_anagram(stringOne, stringTwo):
    print sorted(stringOne) == sorted(stringTwo)

is_anagram(stringOne, stringTwo)

# The question didn't specify whether or not the string had to be actual
# words vetted against a dictionary or something. So if you want to know
# if the two strings are anagrams of each other? They would have to meet
# the same conditions: same letters and that those letters occur in
# the same frequency.  You can easily test these conditions by comparing
# the sorted list of the chars from each string.  If they have the same
# letters in the same frequency, they will produce ordered lists which are
# identical.