# The (so-called) Birthday Paradox:
# 1. Write a function called has_duplicates that takes a list and returns 
# True if there is any element that appears more than once. It should not
# modify the original list. 
# 2. If there are 23 students in your class, what are the chances that two
# of you have the same birthday? You can estimate this probability by 
# generating random samples of 23 birthdays and checking for matches. Hint:
# you can generate random birthdays with the randint function in the random
# module.
# You can read about this problem at wikipedia.org/wiki/Birthday_paradox, 
# and you can see my solution at 
# thinkpython.com/code/birthday.py.
#
import random

listOne = [1, 2, 3, 4, 5]
# listOne = [1, 2, 2, 3, 4]

def has_duplicates(listOne):
   i = 0
   while i < len(listOne):
       if listOne.count(listOne[i]) > 1:
           print True
           break
       elif i == (len(listOne) - 1) and listOne.count(listOne[i]) == 1:
           print False
           break
       i += 1

has_duplicates(listOne)

# for 23 students we will create a list for each of the 23 random birthdays
birthDay = []
 
# to birthDay we will append the random int
i = 0
while i <= 23:
   birthDay.append(random.randint(1, 365))

# we will run the list through has_duplicates(), for each list that returns
# true, increment duplicate count. See what the probibility of getting a 
# duplicate is given 100 trial classes

trial = 0
while trial < 100:
   if has_duplicates():
       dupCount += 1
   trial += 1
   print dupCount / trial
