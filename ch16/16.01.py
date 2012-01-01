# Write a function called print_time that takes a Time object and prints it
# in the form hour:minute:second. Hint: the format sequence '%.2d' prints
# an integer using at least two digits, including a leading zero if necessary.

class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""
    
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

print_time(time)