# Write a class definition for a Date object that has attributes day, month
# and year. Write a function called increment_date that takes a Date object,
# date and an integer, n, and returns a new Date object that represents the
# day n days after date. Hint: "Thirty days hath September..."
# Challenge: does your function deal with leap years correctly? See 
# wikipedia.org/wiki/Leap_year.

# Current Status: Incomplete

rules = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

class Date(object):
    """Representation of a date
    attributes: month, day, year"""
    
date = Date()
date.month = 12
date.day = 31
date.year = 2012
    
def increment(date, inc):
    while True:
        days_left = rules[date.month] - date.day
        if (date.year % 4 == 0) and (date.month == 2):
            rules[date.month] = 29

        # TODO: Make this a switch jeez
        if inc < days_left:
            date.day += inc
            break
        elif inc == 0:
            date.day = rules[date.month]
            break
        elif inc < 0:
            date.day = rules[date.month] + inc
            break
        else:
            inc -= rules[date.month]
            date.month += 1

        if date.month > 12:
            date.year += 1
            date.month = 1
            
    print date.month, date.day, date.year
    
increment(date, 1)