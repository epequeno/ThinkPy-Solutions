# Write a "pure" version of increment that creates and returns a new Time
# object rather than modifying the parameter.

# Current Status: Complete

import copy

class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""
    
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def increment(time, seconds):
    print ("Original time was: %.2d:%.2d:%.2d" 
          % (time.hour, time.minute, time.second))
    
    new_time = copy.deepcopy(time)
    new_time.second += seconds
    if new_time.second > 59:
        quotient, remainder = divmod(new_time.second, 60)
        new_time.minute += quotient
        new_time.second = remainder
    if new_time.minute > 59:
        quotient, remainder = divmod(new_time.minute, 60)
        new_time.hour += quotient
        new_time.minute = remainder
    if new_time.hour > 12:
        new_time.hour -= 12
        
    print "Plus %g seconds" % (seconds)
    print ("New time is: %.2d:%.2d:%.2d" 
          % (new_time.hour, new_time.minute, new_time.second))
    print "memory id of object 'time': ", id(time)
    print "memory id of object 'new_time': ", id(new_time)

increment(time, 300)