# Here's another Car Talk Puzzler you can solve with a search:
# "Recently I had a visit with my mom and we realized that the two digits 
# that make up my age when reversed resulted in her age. For example, if 
# she's 73, I'm 37. We wondered how often this has happened over the years
# but we got sidetracked with other topics and we never came up with an answer.
# "When I got home I figured out that the digits of our ages have been 
# reversible six times so far. I also figured out that if we're lucky it would
# happen again in a few years, and if we're really lucky it would happen one 
# more time after that. In other words, it would have happened 8 times over 
# all. So the question is, how old am I now?"
# Write a Python program that searches for solutions to this Puzzler. Hint: you
# might find the string method zfill useful.
# You can see my solution at thinkpython.com/code/cartalk.py.

# Current Status: Complete

#def make_ages():
#    ages = []
#    for i in range(1, 100):
#        ages.append(str(i).zfill(2))
#    return ages
    
ages = [str(i).zfill(2) for i in range(1, 100)]

def is_palindrome(x, y):
    return x[::-1] == y
    
def main():
    diff = 12
    candidates = []
    while diff <= 45:
        count = 0
        for i in range(0, 99):
            if i + diff > 98:
                break
            elif is_palindrome(ages[i], ages[i + diff]):
                candidates.append((ages[i], ages[i + diff]))
                count += 1
        if count == 8:
            return candidates
        else:
            count = 0
            diff += 1
            candidates = []
    return candidates
    
candidates = main()

print candidates[6][0]