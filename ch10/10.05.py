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

# Current Status: Complete

import random

# listOne = [1, 2, 3, 4, 5]
# listOne = [1, 2, 2, 3, 4]

def has_duplicates(listOne):
   i = 0
   while i < len(listOne):
       if listOne.count(listOne[i]) > 1:
           return True
           break
       elif i == (len(listOne) - 1):
           return False
           break
       i += 1

# has_duplicates(listOne)
# Got rid of the second test on the elif statement. The first if statment will
# check every index from 0 to (len(listOne) - 1) and check if that index has 
# a count greater than 1. If the loop has gotten to the last or even second 
# to last index and not found a duplicate you can be safe in assuming that 
# there are no duplicated items in the list. When the counter is up to the 2nd
# to last item in the list (which as far as the index notation goes is the 
# last item) it means that all items in the list have been checked and that
# there were no matches, the false condition. 

def paradox():
   birthDay = []
   i = 0
   while i <= 23:
       birthDay.append(random.randint(1, 365))
       i += 1
   return birthDay   

# paradox()

# we will run the list through has_duplicates(), for each list that returns
# true, increment duplicate count. See what the probibility of getting a 
# duplicate is given 10,000 trial classes. This one took a while to run with
# 1,000,000 classes.  With 100 trials the probility was kind of all over the
# place and we would have had to do some other statistics on it to find the
# average or mode, but if we change the sample size to 10,000, the probablity
# returns ~50% on most runs.

def stats(paradox):
   i = 0
   dupCount = 0
   while i < 10000:
       if has_duplicates(paradox()):
           dupCount += 1
       i += 1 
   print (float(dupCount) / i) * 100.0, '%'


stats(paradox)

# His solution is better since it takes the class size and number of trials
# as variables. Parts of his solution and mine are almost identical but the
# way we approached the has_duplicates problem are pretty different.
#
# When run with 10,000 trials stats() runs:
# real	0m0.541s
# user	0m0.540s
# sys	0m0.000s
#
# When run with 100,000 trials:
# real	0m5.223s
# user	0m5.204s
# sys	0m0.000s
#
# With 1,000,000 trials:
# real	0m52.642s
# user	0m52.451s
# sys	0m0.020s
# 
# Setting these as benchmarks for attempts at optimization later.
