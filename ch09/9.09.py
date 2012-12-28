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

ages = [str(i).zfill(2) for i in range(1, 100)]  # moms max age @ 99


def is_palindrome(x, y):
    return x[::-1] == y


def main():
    diff = 15  # moms age @ child birth from 15 to 45
    while diff <= 45:
        palindromes = []
        for i in range(0, 99):
            if (i + diff) >= 99:  # IndexErr in ages fix
                pass
            elif is_palindrome(ages[i], ages[i + diff]):
                palindromes.append(ages[i])
        if len(palindromes) == 8:
            return palindromes
        else:
            diff += 1

candidates = main()

print "You are now %s years old." % candidates[5]