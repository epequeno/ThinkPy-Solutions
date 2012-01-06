# Write a str method for the Point class. Create a Point object and print it.

# Current Status: Complete

class Point(object):
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
        
point = Point()
print point

point = Point(10)
print point

point = Point(10, 15)
print point