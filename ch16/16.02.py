# Write a boolean function called is_after that takes two Time objects,
# t1 and t2, and returns True if t1 follows t2 chronologically and False
# otherwise. Challenge: don't use an if statement.

# Current Satus: Incomplete

import datetime

class Time(object):
    def __init__(self, year=2000, month=1, day=1, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)
        
        
