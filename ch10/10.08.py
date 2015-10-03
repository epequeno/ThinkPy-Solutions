# To check whether a word is in the word list, you could use the in operator,
# but it would be slow because it searches through the words in order.
# Because the words are in alphabetical order, we can speed things up with a
# bisection search (also known as binary search), which is similar to what
# you do when you look a word up in the dictionary. You start in the middle
# and check to see whether the word you are looking for comes before the word
# in the middle of the list. If so, then you search the first half of the
# list the same way. Otherwise you search the second half.
# Either way, you cut the remaining search space in half. If the word list
# has 113,809 words, it will take about 17 steps to find the word or conclude
# that it's not there.
# Write a function called bisect that takes a sorted list and a target value
# and returns the index of the value in the list, if it's there, or None if
# it's not.
# Or you could read the documentation of the bisect module and use that!

# Current Status: Complete

with open('words.txt') as fd:
    word_list = fd.read().splitlines()


def bisect(myWord, myList):
    original = myList
    while True:
        middle = len(myList) / 2
        if myWord > myList[middle]:
            myList = myList[middle:]
        elif myWord < myList[middle]:
            myList = myList[:middle]
        elif myWord == myList[middle]:
            return original.index(myWord)

        if len(myList) == 1:
            if myWord != myList[:]:
                return None
            else:
                return original.index(myWord)


print bisect("danger", word_list)