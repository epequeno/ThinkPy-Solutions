# Write a function called distance that takes two Points as arguments and
# returns the distance between them.

# Current Status: Complete

import math


class Point(object):
    """Represents a point in 2d space."""

point_one = Point()
point_two = Point()

point_one.x, point_one.y = 6.0, 1.0
point_two.x, point_two.y = 2.0, 6.0


def distance(p1, p2):
    """Returns the distance between two points in 2d space."""
    delta_x = p2.x - p1.x
    delta_y = p2.y - p1.y
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

print "The distance between point one at (%g,%g)" % (point_one.x, point_one.y),
print "and point two at (%g,%g)" % (point_two.x, point_two.y),
print "is %.3f" % distance(point_one, point_two)