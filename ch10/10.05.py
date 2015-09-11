# The (so-called) Birthday Paradox:
# 1. Write a function called has_duplicates that takes a list and returns
# True if there is any element that appears more than once. It should not
# modify the original list.
# 2. If there are 23 students in your class, what are the chances that two
# of you have the same birthday? You can estimate this probability by
# generating random samples of 23 birthdays and checking for matches. Hint:
# you can generate random birthdays with the randint function in the random
# module.
# You can read about this problem at wikipedia.org/wiki/Birthday_paradox,
# and you can see my solution at
# thinkpython.com/code/birthday.py.

# Current Status: Complete
# Notes: View version history

import random

NUMBER_OF_STUDENTS = 23
TRIALS = 1000


def has_duplicates(my_list):
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1


def generate_random_birthdays():
    return [random.randint(1, 365) for student in range(NUMBER_OF_STUDENTS)]


def stats(TRIALS):

    duplicate_count = 0
    for i in range(TRIALS):
        if has_duplicates(generate_random_birthdays()):
            duplicate_count += 1
    print "In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (TRIALS, NUMBER_OF_STUDENTS, (float(duplicate_count) / TRIALS) * 100)


stats(TRIALS)