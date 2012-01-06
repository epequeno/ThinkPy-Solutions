# Write a function that reads the file words.txt and builds a list with one 
# element per word. Write two versions of this function, one using the 
# append method and the other using the idiom t = t + [x]. Which one takes
# longer to run? Why?
# You can see my solution at thinkpython.com/code/wordlist.py.

# Current Status: Complete

words = open('words.txt')

def method_one(words):
   wordList = []
   for line in words:
       line = line.strip()
       wordList.append(line)
   print len(wordList)
   print wordList[:10]

method_one(words)

# using the GNU/Linux tool 'time' method_one produced this:
# real   0m0.078s
# user   0m0.060s
# sys    0m0.012s 

def method_two(words):
   wordList = []
   for line in words:
       line = line.strip()
       wordList += [line]
   print len(wordList)
   print wordList[:10]

# method_two(words)

# To be honest, I couldn't tell the difference between the two runs. I 
# don't know how to tell the system to measure these things at the moment.
# I even added the str.strip() method which seemed to gum things up a bit
# but kept both of them about equal to each other as far as I could tell.

# time produced this for method_two:
# real  0m0.054s
# user  0m0.040s
# sys   0m0.012s

# method_two won the race. method_two probably goes a bit faster because 
# concatenation is a more simple operation but isn't the append method 
# also simply concatenating? 
