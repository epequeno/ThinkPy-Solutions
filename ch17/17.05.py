# Write an add method for Points that works with either a Point object or a 
# tuple:
# -If the second operand is a Point, the method should return a new Point 
# whose x coordinate is the sum of the x coordinates of the operands, and 
# likewise for the y coordinates.
# -If the second operand is a tuple, the method should add the first element 
# of the tuple to the x coordinate and the second element to the y coordinate,
# and return a new Point with the result.

# Current Status: Complete

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        point_ = Point()
        if isinstance(other, Point):
            point_.x += self.x + other.x
            point_.y += self.y + other.y
            return point_
        elif type(other) == tuple:
            point_.x += self.x + other[0] 
            point_.y += self.y + other[1]
        return point_
    
    def __radd__(self, other):
        return self.__add__(other)
        
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
        
point1 = Point(1, 6)
point2 = (5, 2)
point3 = point1 + point2
point4 = point2 + point1
print point3, point4