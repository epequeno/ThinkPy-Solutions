# Here's another Car Talk Puzzler:
# "I was driving on the highway the other day and I happened to notice 
# my odometer. Like most odometers, it shows six digits, in whole miles 
# only. So, if my car had 300,000 miles, for example, I'd see 3-0-0-0-0-0.
# "Now, what I saw that day was very interesting. I noticed that the last 
# 4 digits were palindromic; that is, they read the same forward as backward.
# For example, 5-4-4-5 is a palindrome, so my odometer could have read 
# 3-1-5-4-4-5. "One mile later, the last 5 numbers were palindromic. For 
# example, it could have read 3-6-5-4-5-6. One mile after that, the middle 
# 4 out of 6 numbers were palindromic. And you ready for this? One mile later,
# all 6 were palindromic! "The question is, what was on the odometer when I 
# first looked?"
# Write a Python program that tests all the six-digit numbers and prints any
# numbers that satisfy these requirements. You can see my solution at 
# thinkpython.com/code/cartalk.py.

# Current Status: Complete

def is_pal_num():
   for i in range(100000, 1000000):
       if str(i)[2:] == str(i)[:1:-1]: # last 4 
           i += 1
           if str(i)[1:] == str(i)[5:0:-1]: # last 5
               i += 1
               if str(i)[1:-1] == str(i)[-2:0:-1]: # middle 4
                   i += 1
                   if str(i) == str(i)[::-1]: # all 6
                       print i - 3  
                   
is_pal_num()

# My solution is much different from the authors solution. For exercize
# 9.7 I couldn't get a solution and look at the authors and ended up with 
# a solution that was almost identical. In this case I solved it independently
# and got something totally different.  I kind of like mine a little better
# since it's easier to follow the logic assuming the index notation doesn't
# throw you off. Simply put: check if each condition is true, if it is 
# add another mile then move on to the next if statement until all conditions
# are met, then print the number minus the 3 added miles. The two values 
# which satisfy the conditions are 198888 and 199999.
