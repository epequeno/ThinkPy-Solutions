# Rewrite increment using time_to_int and int_to_time.

# Current Status: Complete

import copy

class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""
    
time = Time()
time.hour = 11
time.minute = 59
time.second = 30
    
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
    
def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def increment(time, seconds):
    new_time = copy.deepcopy(time)
    new_time = time_to_int(new_time) + seconds
    new_time = int_to_time(new_time)
    print ("New time is: %.2d:%.2d:%.2d" 
          % (new_time.hour, new_time.minute, new_time.second))
    
increment(time, 300)