# Write an init method for the Point class that takes x and y as optional
# parameters and assigns them to the corresponding attributes.

# Current Status: Complete

class Point(object):
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
        
    def print_point(self):
        print "x =", self.x, ",",
        print "y =", self.y
        
point = Point()
point.print_point()

point = Point(10)
point.print_point()

point = Point (20, 30)
point.print_point()