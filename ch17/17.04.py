# Write an add method for the Point class.

class Point(object):
    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(%d, %d)' % (self.x, self.y)
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point
        
point1 = Point(1, 3)
point2 = Point(4, 5)

print point1 + point2