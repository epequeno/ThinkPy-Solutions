#a = raw_input('Side a?\n')
#b = raw_input('Side b?\n')
#c = raw_input('Side c?\n')
#
#def is_triangle(a, b, c):
#   for i in [a, b, c]:
#       i = float(i)
#       print i
#       print a, b, c
#   if (a > (b + c) or
#       b > (a + c) or
#       c > (a + b)):
#       print 'Not gonna happen buddy'
#   else:
#       print 'You got yourself a triangle there.'

#is_triangle(a, b ,c)

# version 2:
a = int(raw_input("A = "))
b = int(raw_input("B = "))
c = int(raw_input("C = "))

triangle = [a, b, c]
triangle.sort()

def is_triangle():
    if triangle[0] + triangle[1] <= triangle[2]:
        print 'No'
    else:
        print 'Yes'
        
is_triangle()