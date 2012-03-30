# The datetime module provides date and time objects that are similar to the
# Date and Time objects in this chapter, but they provide a rich set of methods
# and operators. Read the documentation at 
# docs.python.org/lib/datetime-date.html.
# 1. Use the datetime module to write a program that gets the current date and
# prints the day of the week.
# 2. Write a program that takes a birthday as input and prints the user's age
# and the number of days, hours, minutes and seconds until their next birthday.

# Current Status: incomplete

import datetime

rules = {0:"Sunday",
         1:"Monday",
         2:"Tuesday",
         3:"Wednesday",
         4:"Thursday",
         5:"Friday",
         6:"Saturday"}

class Time(object):
    now = datetime.datetime.now()
    
    def __init__(self, year=1, month=01, day=01, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)
    
today = Time().now
birthday = Time(1983, 4, 13, 0, 0, 0).date

def day_of_week():
    return "1) Today is %s" % rules[today.weekday()]

def birthday_stats(birthday):
    age = today.year - birthday.year    
    
    if (birthday.month >= today.month):
        if (birthday.day <= today.day):
            pass
        else:
            age -= 1
            
    birthday_ = Time(today.year, birthday.month, birthday.day).date
    till_birthday = str(today - birthday_).split()
    
    if len(till_birthday) > 1:
        days = int(till_birthday[0])
        time = till_birthday[2].split(":")
    else:
        days = 365
        time = till_birthday[0].split(":")
    
    hours = time[0]
    mins = time[1]
    secs = time[2][:2]
    
    if (days > 0) and (days != 365):
        days = 365 - days
    else:
        days = abs(days)
        
    print "2) You are %s years old; %sd:%sh:%sm:%ss until your next birthday." \
    % (age, days, hours, mins, secs)
        

print day_of_week()
birthday_stats(birthday)