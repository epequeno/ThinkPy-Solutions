# Write a class definition for a date object that has attributes day, month
# and year. Write a function called increment_date that takes a date object,
# date and an integer, n, and returns a new date object that represents the
# day n days after date. Hint: "Thirty days hath September..."
# Challenge: does your function deal with leap years correctly? See 
# wikipedia.org/wiki/Leap_year.

# Current Status: Complete

rules = {1:31,
         2:28,
         3:31,
         4:30,
         5:31,
         6:30,
         7:31,
         8:31,
         9:30,
         10:31,
         11:30,
         12:31}

names = {1:"January",
         2:"Feburary",
         3:"March",
         4:"April",
         5:"May",
         6:"June",
         7:"July",
         8:"August",
         9:"September",
         10:"October",
         11:"November",
         12:"December"}


class date(object):
    """Representation of a date
    attributes: month, day, year"""
    
date = date()
date.month = 10
date.day = 30
date.year = 2012

def increment_date(date, inc):
    date_ = date
    if (date_.year % 4 == 0):
        print "Starting: %s %s, %s (Leap year!)" \
        % (names[date.month], date.day, date.year)
    else:
        print "Starting: %s %s, %s" % (names[date.month], date.day, date.year)
    print "Moving forward %s days" %  inc
    while True:
        rules[2] = 28
        if (date_.year % 4 == 0):
            rules[2] = 29
        elif date_.month != 2:
            pass
    
        days_left = rules[date_.month] - date_.day

        if inc <= days_left:
            date_.day += inc
            break
        elif inc == 0:
            date_.day = rules[date_.month]
            break
        elif inc < 0:
            date_.day = rules[date_.month] + inc
            break
        else:
            inc -= rules[date_.month]
            date_.month += 1

        if date_.month > 12:
            date_.year += 1
            date_.month = 1
    if ((date_.year - 1) % 4 == 0) and date_.month != 2:
        date_.day -= 1
    print "Ending: %s %s, %s" % (names[date_.month], date_.day, date_.year)
    
increment_date(date, 365)