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

class today(object):
    def __init__(self):
        self.date = datetime.datetime.today()
        self.weekday = self.date.weekday()
        self.day = self.date.day
        self.year = self.date.year
        self.month = self.date.month
        self.time = self.date.time
        self.second = self.date.second
        self.datetime = datetime.datetime(self.year,
                                          self.month,
                                          self.day,
                                          self.time().hour,
                                          self.time().minute,
                                          self.time().second)
        
class birthday(object):
    def __init__(self, 
                 year=2000, 
                 month=01,
                 day=01,
                 hour=0,
                 minute=0,
                 second=0):
        self.date = datetime.datetime(year,
                                      month,
                                      day,
                                      hour,
                                      minute,
                                      second)
        self.year = self.date.year
        self.weekday = self.date.weekday()
        self.day = self.date.day
        self.year = self.date.year
        self.month = self.date.month
        self.time = self.date.time
                
date = today()

rules = {0:"Monday",
         1:"Tuesday",
         2:"Wednesday",
         3:"Thursday",
         4:"Friday",
         5:"Saturday",
         6:"Sunday"}

def print_day():
    print "Today is %s" % rules[date.weekday]

print_day()

test_birthday = birthday(1980, 3, 1)

def print_birthday(test_birthday):
    this_year = date.year
    this_month = date.month
    if test_birthday.date.month > this_month:
        age = (this_year - 1) - test_birthday.year
    else:
        age = this_year - test_birthday.year
    print "You are %s years old." % age
    
    tmp_birthday = birthday(this_year,
                            test_birthday.month,
                            test_birthday.day)
    
    till_birthday = tmp_birthday.date - date.datetime
    
    if till_birthday.total_seconds() < 0:
        tmp_birthday = birthday(this_year + 1,
                                test_birthday.month,
                                test_birthday.day)
        till_birthday = tmp_birthday.date - date.datetime
        print till_birthday, "until your next birthday!"
    else:
        print till_birthday, "until your next birthday!"
    
print_birthday(test_birthday)   