# If you are given three sticks, you may or may not be able to arrange 
# them in a triangle. For example, if one of the sticks is 12 inches long and 
# the other two are one inch long, it is clear that you will not be able to
# get the short sticks to meet in the middle. For any three lengths, there is
# a simple test to see if it is possible to form a triangle:
# "If any of the three lengths is greater than the sum of the other two, then
# you cannot form a triangle. Otherwise, you can."
# 1. Write a function named is_triangle that takes three integers as 
# arguments, and that prints either "Yes" or "No," depending on whether you
# can or cannot form a triangle from sticks with the given lengths.
# 2. Write a function that prompts the user to input three stick lengths,
# converts them to integers, and uses is_triangle to check whether sticks with
# the given lengths can form a triangle.

# Current Status: Complete

triangle = [int(raw_input(x)) for x in ['a = ', 'b = ', 'c = ']]
triangle.sort()


def is_triangle():
    if triangle[0] + triangle[1] <= triangle[2]:
        print 'No'
    print 'Yes'
        
is_triangle()