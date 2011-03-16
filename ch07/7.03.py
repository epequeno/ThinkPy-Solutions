# function to test newton's method vs. math.sqrt() 

import math

def newtons(n):
   n = float(n) # convert input to float so printout() doesn't have to
   x = n / 2 # rough estimate
   i = 0
   while i < 10:
       y = (x + n / x) / 2 # newtons method
       x = y
       i += 1
   return y

def libmath(n):
   n = float(n) 
   return math.sqrt(n)

# this function has a mix of int, str and float so there is a bit of 
# conversion going on.

def printout():
   for i in range(1, 10): 
       n = str(newtons(i)) # newtowns() gets int and returns float. change to str.
       l = str(libmath(i))  # same here
       ab = abs(newtons(i) - libmath(i)) # out as int in as float, no str
       if (len(n) or len(l)) == 3:
           print i, n, '         ', l, '          ', ab
       elif len(n) == 12:
           print i, n, '', l, ' ', ab
       else:
           print i, n, l, '', ab

printout()  
