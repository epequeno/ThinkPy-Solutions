# Write a boolean function called is_after that takes two Time objects,
# t1 and t2, and returns True if t1 follows t2 chronologically and False
# otherwise. Challenge: don't use an if statement.

# Current Satus: Complete

import time
import datetime

class Time(object):
    """Time object based on datetime.datetime describes time in 24hr format"""
    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)
        
    def mktime(self):
        return time.mktime(self.date.timetuple())
        
        
t1 = Time(2013, 1, 3, 15)
t2 = Time(2013, 1, 3, 1)

def is_after(time1, time2):
    return time1.mktime() > time2.mktime()
    
print is_after(t1, t2)