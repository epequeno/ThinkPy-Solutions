# Read the following function and see if you can figure out what it does. 
# Then run it (see the examples in Chapter 4).

# Current Status: Complete

def draw(t, length, n):
   if n == 0:
       return
   angle = 50
   fd(t, length*n)
   lt(t, angle)
   draw(t, length, n-1)
   rt(t, 2*angle)
   draw(t, length, n-1)
   lt(t, angle)
   bk(t, length*n)