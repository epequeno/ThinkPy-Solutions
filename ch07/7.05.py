# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:17:35 2011

@author: steven
"""

# The brilliant mathematician Srinivasa Ramanujan found an infinite series
# that can be used to generate a numerical approximation of pi:
# http://en.wikipedia.org/wiki/Srinivasa_Ramanujan#Mathematical_achievements
#
# Write a function called estimate_pi that uses this formula to compute and
# return an estimate of pi. It should use a while loop to compute terms of
# the summation until the last term is smaller than 1e-15 (which is Python
# notation for 10^−15 ). You can check the result by comparing it to math.pi.
# You can see my solution at thinkpython.com/code/pi.py.

# Current Status: Complete

import math


def estimate_pi():
    k = 0.0
    last_term = 1.0
    sigma = 0
    while last_term > 1e-15:
        last_term = ((math.factorial(4.0 * k)) * (1103.0 + 26390.0 * (k))) \
        / ((math.factorial(k) ** 4.0) * (396.0 ** (4.0 * k)))
        k += 1.0
        sigma += last_term
    result = ((2 * math.sqrt(2)) / 9801) * sigma
    return 1 / result

print estimate_pi()
print math.pi

# real    0m0.014s
# user    0m0.004s
# sys     0m0.008s