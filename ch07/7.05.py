# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 20:17:35 2011

@author: steven
"""

# The brilliant mathematician Srinivasa Ramanujan found an infinite series 
# that can be used to generate a numerical approximation of pi:
# http://en.wikipedia.org/wiki/Srinivasa_Ramanujan#Mathematical_achievements
# Write a function called estimate_pi that uses this formula to compute and 
# return an estimate of pi. It should use a while loop to compute terms of
# the summation until the last term is smaller than 1e-15 (which is Python 
# notation for 10−15 ). You can check the result by comparing it to math.pi.
# You can see my solution at thinkpython.com/code/pi.py.