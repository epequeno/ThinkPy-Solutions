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
    pow = b(sum) ** 2
    return pow

x = 1
y = x + 1
print c(x, y + 3, x + y)

# The program prints 8100. c() calls b() with the sum of 1, 5, 3 which is 9.
# b() then calls a(9, 9). The first 9 has 1 added to it so a returns
# 10 * 9 = 90. b() returns 90 to c() and c() sqaures it so c() returns 8100.