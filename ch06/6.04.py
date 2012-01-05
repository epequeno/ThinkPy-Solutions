# Exercise 6.4 Draw a stack diagram for the following program. What does the 
# program print?

# Current Status: Complete

def b(z):
    prod = a(z, z)
    print z, prod
    return prod
    
def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    sum = x + y + z
    pow = b(sum)**2
    return pow

x = 1
y = x + 1
print c(x, y+3, x+y)