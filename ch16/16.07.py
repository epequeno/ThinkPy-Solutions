# Write a class definition for a Date object that has attributes day, month
# and year. Write a function called increment_date that takes a Date object,
# date and an integer, n, and returns a new Date object that represents the
# day n days after date. Hint: "Thirty days hath September..."
# Challenge: does your function deal with leap years correctly? See 
# wikipedia.org/wiki/Leap_year.

# Current Status: Incomplete

class Date(object):
    """Representation of a date
    attributes: month, day, year"""
    
date = Date()
date.month = 1
date.day = 1
date.year = 2012
    
def increment_date(date, increment):
    if date.month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_month = 31
    elif date.month == 2:
        days_in_month = 28
    else:
        days_in_month = 30
    new_date = days_in_month + date.day + increment
    print days_in_month
    
increment_date(date, 30)