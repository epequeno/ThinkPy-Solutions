# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding 
# dx to the x coordinate of corner and adding dy to the y coordinate of corner.

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
    """Takes a rectangle and moves it to the values of dx and dy."""
    print ("The rectangle started with bottom left corner at (%g,%g)" 
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and top right corner at (%g,%g)." 
           % (rectangle.corner2.x, rectangle.corner2.y)),
    print "dx is %g and dy is %g" % (dx, dy)
    rectangle.corner1.x = rectangle.corner1.x + dx
    rectangle.corner2.x = rectangle.corner2.x + dx
    rectangle.corner1.y = rectangle.corner1.y + dy
    rectangle.corner2.y = rectangle.corner2.y + dy
    print ("It ended with a bottom left corner at (%g,%g)" 
           % (rectangle.corner1.x, rectangle.corner1.y)),
    print ("and a top right corner at (%g,%g)" 
           % (rectangle.corner2.x, rectangle.corner2.y))
    
    
move_rectangle(rectangle, dx, dy)