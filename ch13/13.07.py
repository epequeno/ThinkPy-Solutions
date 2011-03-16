# This algorithm works, but it is not very efficient; each time you choose a
# random word, it rebuilds the list, which is as big as the original book.
# An obvious improvement is to build the list once and then make multiple 
# selections, but the list is still big.
# An alternative is:
# 1. Use keys to get a list of the words in the book.
# 2. Build a list that contains the cumulative sum of the word frequencies
# (see Exercise 10.1). The last item in this list is the total number of
# words in the book, n.
# 3. Choose a random number from 1 to n. Use a bisection search (See Exercise 
# 10.8) to find the index where the random number would be inserted in the 
# cumulative sum.
# 4. Use the index to find the corresponding word in the word list.
# Write a program that uses this algorithm to choose a random word from the 
# book.

