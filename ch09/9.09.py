# Here's another Car Talk Puzzler you can solve with a search:
# "Recently I had a visit with my mom and we realized that the two digits 
# that make up my age when reversed resulted in her age. For example, if 
# she's 73, I'm 37. We wondered how often this has happened over the years
# but we got sidetracked with other topics and we never came up with an answer.
# "When I got home I figured out that the digits of our ages have been 
# reversible six times so far. I also figured out that if we're lucky it would
# happen again in a few years, and if we're really lucky it would happen one 
# more time after that. In other words, it would have happened 8 times over 
# all. So the question is, how old am I now?"
# Write a Python program that searches for solutions to this Puzzler. Hint: you
# might find the string method zfill useful.
# You can see my solution at thinkpython.com/code/cartalk.py.

# Current Status: Incomplete

import string

def ages():
   age = 0
   while age < 200:
       newAge = str(age).zfill(2)
       newAge2 = str(age + 36)
       if newAge[1] == newAge2[0] and newAge[0] == newAge2[1]:
           print newAge, newAge2
       age += 1
ages()