# Exercise 6.8 The greatest common divisor (GCD) of a and b is the largest
# number that divides both of them with no remainder 
# One way to find the GCD of two numbers is Euclid's algorithm, which
# is based on the observation that if r is the remainder when a is divided by
# b, then gcd(a, b) = gcd(b, r). As a base case, we can consider gcd(a, 0) = a.
# Write a function called gcd that takes parameters a and b and returns their
# greatest common divisor.
# If you need help, see en.wikipedia.org/wiki/Euclidean_algorithm.

# Current Status: Incomplete

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)
        
print gcd(1989, 867)