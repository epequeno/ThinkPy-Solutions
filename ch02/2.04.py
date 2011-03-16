# Practice using the Python interpreter as a calculator:
#
# 1. The volume of a sphere with radius r is 4/3*(pi)r^3 . What is the volume of
# a sphere with radius 5?
# Hint: 392.6 is wrong!

radius = 5.0

def volume(radius):
   volume = ((4.0 / 3.0) * (3.14) * (radius)**3) 
   print 'The volume is: ', volume

volume(radius)

# Solution: If you use integers for this problem you will be off by about 1/3
# if you evaluate 4/3 as ints it will produce 1 as a result when the value
# that you are looking for is 1.33 repeating. Thats a signifigant difference.
# The answer you get with using floats is 523.33. 

# 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% 
# discount. Shipping costs $3 for the first copy and 75 cents for each 
# additional copy. What is the total wholesale cost for 60 copies?

bookCost = 24.95
numBooks = 60.0

def cost(numBooks):
   bulkBookCost = ((bookCost * 0.60) * numBooks)
   shippingCost = (3.0 + (0.75 * (numBooks - 1)))
   totalCost = bulkBookCost + shippingCost
   print 'The total cost is: $', totalCost

cost(numBooks)

# This one is slippery because of the wording. If the cost of the book is 
# 24.95 with a 40% discount you may be tempted to try this 24.95*.40 which 
# will actually give you the amount you save. To determine cost you'd have 
# to do this 24.95*.60 since you will be paying 60% of the retail cost.
# I made a mistake the first time by using numBooks to determine shipping
# cost, I needed to use (numBooks - 1) since the cost of the first book is
# predetermined and the 0.75 cent is for the rest of the order, minus one.
#
# 3. If I leave my house at 6:52 am and run 1 mile at an easy pace 
# (8:15 per mile), then 3 miles at tempo (7:12 per mile) and 1 mile at easy 
# pace again, what time do I get home for breakfast?

import datetime
from datetime import timedelta

startTime = datetime.datetime(2011, 01, 01, 6, 52, 0)
# set datetime y/m/d h:m:s:ms tzinfo
timeSec = (((8.0 * 60.0) + 15.0) * 2.0) + (((7.0 * 60.0) + 12.0) * 3.0)
timeMin = timeSec / 60.0
# not printed, result is 38.1; a 1/10 of a min is 6 seconds
timeSpent = datetime.timedelta(minutes=38, seconds=6)
finalTime = startTime + timeSpent

print 'You get home at: ', finalTime

# This one took a while because of the time addition, in chapter 2 you don't
# know about imports or methods as used in this solution but I wanted to get
# some practice with the datetime and timedelta modules.  I got stuck because 
# you can use datetime.time(h, m, s) to create 06:52:00 but timedelta only 
# adds with datetime.date. So I just set an arbitrary date of
# 2011-01-01 06:52:00. Adding the 38.1 mins (or 38 min 6 sec) takes us to the
# return time of 07:30:06.  Although really the problem is a bit too vauge, 
# they dont' specify whether the trip is one way or round-trip if it is round
# trip you're going to have to double timedelta.   
