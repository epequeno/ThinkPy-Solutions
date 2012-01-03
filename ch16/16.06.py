# Write a function called mul_time that takes a Time object and a number and
# returns a new Time object that contains the product of the original Time and
# the number.
# Then use mul_time to write a function that takes a Time object that 
# represents the finishing time in a race, and a number that represents the 
# distance, and returns a Time object that represents the average pace (time
# per mile).

# Current Status: Complete

class Time(object):
    """ represents the time of day.
    attributes: hour, minute, second"""
    
time = Time()
time.hour = 3
time.minute = 0
time.second = 0

def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
    
def int_to_time(seconds):
    new_time = Time()
    minutes, new_time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def mul_time(time, multicand):
    time_int = time_to_int(time) * multicand
    new_time = int_to_time(time_int)
    if new_time.hour > 12:
        new_time.hour = new_time.hour % 12
#    print ("New time is: %.2d:%.2d:%.2d" 
#    % (new_time.hour, new_time.minute, new_time.second))
    return new_time
    
# mul_time(time, 2)

def race_stats(time, distance):
    print ("The finish time was %.2d:%.2d:%.2d" 
          % (time.hour, time.minute, time.second))
    print "The distance was %d miles" % (distance)
    
    average = mul_time(time, (1.0 / distance))
    
    print ("The average is: %.2d:%.2d:%.2d per mile"
          % (average.hour, average.minute, average.second))
    
race_stats(time, 3)