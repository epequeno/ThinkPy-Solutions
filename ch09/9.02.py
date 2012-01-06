# In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby 
# that does not contain the letter "e." Since "e" is the most common letter
# in English, that's not easy to do. In fact, it is difficult to construct
# a solitary thought without using that most common symbol. It is slow going
# at first, but with caution and hours of training you can gradually gain 
# facility.
# All right, I'll stop now.
# Write a function called has_no_e that returns True if the given word
# doesn't have the letter "e" in it.
# Modify your program from the previous section to print only the words 
# that have no "e" and compute the percentage of the words in the list have 
# no "e."

# Current Status: Complete

word = open('words.txt')

def words(word):
    i = 0
    t = 0
    for line in word:
        if line.find('e') == -1:
            print line
            i += 1
        t += 1
    percent  = (float(i) / float(t)) * 100.0
    print percent, '%'

words(word)