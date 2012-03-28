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
    
    def __init__(self, year=2000, month=01, day=01, hour=0, minute=0, second=0):
        self.date = datetime.datetime(year, month, day, hour, minute, second)
    
now = Time()
birthday = Time(1983, 12, 13, 12, 0, 0)

def day_of_week():
    day = now.now.weekday()
    return "Today is %s" % rules[day]

def birthday_stats(birthday):
    age = now.now.year - birthday.date.year
    if now.now.month <= birthday.date.month:
        age -= 1
    print "You are %s years old." % age
    
    time_till = now.now - birthday.date
    print "There are %s days," % (time_till.days - (age * 365))    
    answer = str(time_till).split()[2]
    answer = answer.split(":")
    print answer[0] + " hours,"
    print answer[1] + " mins, and"
    print answer[2][:2] + " seconds until your next birthday."
    
    
print day_of_week()
birthday_stats(birthday)