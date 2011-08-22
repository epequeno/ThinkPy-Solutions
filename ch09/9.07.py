# This question is based on a Puzzler that was broadcast on the radio program
# Car Talk: Give me a word with three consecutive double letters. I'll give
# you a couple of words that almost qualify, but don't. For example, the word
# committee, c-o-m-m-i-t-t-e-e. It would be great except for the 'i' that
# sneaks in there. Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take 
# out those i's it would work. But there is a word that has three consecutive
# pairs of letters and to the best of my knowledge this may be the only word.
# Of course there are probably 500 more but I can only think of one. What 
# is the word? Write a program to find it. You can see my solution at 
# thinkpython.com/code/cartalk.py.
#
wordList = open('words.txt')

def is_trip_pair(wordList):
   for word in wordList:
       i = 0
       pairCount = 0
       while i < len(word) - 1:
           if word[i] == word[i + 1]:
               pairCount += 1
               if pairCount == 3:
                   print word
               i += 2
           else: 
               pairCount = 0
               i += 1
           
is_trip_pair(wordList)

# This is essentially the solution that the author of Think Python provided
# I just modified it a bit and got rid of the last 'return False' statement 
# at the bottom, as I read it, that will print out False for every word in 
# the list regardless if conditions are met or not.  The way that I've written
# it here will print the word.  The way the author wrote it is a little 
# strange since that's more of a test given a word as an input. By adding
# the 'for' loop I can check the entire wordList for the conditions.
# There are 4 words in the list that meet the condition of 3 consecutive 
# pairs of letters, all variants of bookkeep. 
