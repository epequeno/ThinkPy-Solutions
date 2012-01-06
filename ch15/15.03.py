# Write a version of move_rectangle that creates and returns a new Rectangle
# instead of modifying the old one.

# Current Status: Complete

import copy

class Point(object):
    """Represents a point in 2d space"""
    
class Rectangle(object):
    """Represents a rectangle in 2d space"""
    
rectangle = Rectangle()

bottom_left = Point()
bottom_left.x = 3.0
bottom_left.y = 5.0

top_right = Point()
top_right.x = 5.0
top_right.y = 10.0

rectangle.corner1 = bottom_left
rectangle.corner2 = top_right

dx = 5.0
dy = 12.0

def move_rectangle(rectangle, dx, dy):
    """Moves a trangle to the values of dx and dy using deepcopy to create
    a new rectangle object and not modify the original rectangle."""
    new_rectangle = copy.deepcopy(rectangle)
    print ("Original: (%g,%g)" % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("(%g,%g)" % (rectangle.corner2.x, rectangle.corner2.y))
    new_rectangle.corner1.x = new_rectangle.corner1.x + dx
    new_rectangle.corner2.x = new_rectangle.corner2.x + dx
    new_rectangle.corner1.y = new_rectangle.corner1.y + dy
    new_rectangle.corner2.y = new_rectangle.corner2.y + dy
    print ("New: (%g,%g)" % (new_rectangle.corner1.x, new_rectangle.corner1.y)),
    print ("(%g,%g)" % (new_rectangle.corner2.x, new_rectangle.corner2.y))
    
move_rectangle(rectangle, dx, dy)