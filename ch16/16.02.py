# Write a boolean function called is_after that takes two Time objects,
# t1 and t2, and returns True if t1 follows t2 chronologically and False
# otherwise. Challenge: don't use an if statement.

# Current Satus: Complete

import datetime

class Time(object):
    """Time object based on datetime.datetime describes time in 24hr format"""
    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)
        
    def time_to_int(self):
        return int(self.date.strftime("%s"))

# 1 AM on Jan 1, 2001        
t1 = Time(2001, 1, 1, 1)

# 12 AM on Jan 1, 2001
t2 = Time(2001, 1, 1, 0)


def is_after(time1, time2):
    return time1.time_to_int() > time2.time_to_int()
    
print is_after(t2, t1)
