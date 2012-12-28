# Write a __cmp__ method for Time objects. Hint: you can use tuple comparison,
# but you also might consider using integer subtraction.

# Current Status: Incomplete


class Time(object):
    def __init__(self, hour=0, min=0):
        self.hour = hour
        self.min = min
        
    def __cmp__(self,)