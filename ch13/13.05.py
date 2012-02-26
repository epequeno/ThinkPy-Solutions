#Write a function named choose_from_hist that takes a histogram as defined in
# Section 11.1 and returns a random value from the histogram, chosen with
# probability in proportion to frequency. For example, for this histogram:
#
#>>> t = ['a', 'a', 'b']
#>>> h = histogram(t)
#>>> print h
#{'a': 2, 'b': 1}
#your function should 'a' with probability 2/3 and 'b' with probability 1/3.

import random

t = ['a', 'a', 'b']

def hist(x):
    hist = {}
    for item in x:
        hist[item] = hist.get(item, 0) + 1
    return hist
    
hist = hist(t)

def choose_from_hist(hist):
    list_ = []
    for key in hist:
        for i in range(0, hist[key]):
            list_.append(key)
    return random.choice(list_)
    
def stats():
    a = 0
    b = 0
    for i in range(0, 10000):
        if choose_from_hist(hist) == 'a':
            a += 1
        else:
            b += 1
    print "a: %.5f" % (a / 10000.0), "b: %.5f" % (b / 10000.0)
    
stats()