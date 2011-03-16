# Write a function that reads the file words.txt and builds a list with one 
# element per word. Write two versions of this function, one using the 
# append method and the other using the idiom t = t + [x]. Which one takes
# longer to run? Why?
# You can see my solution at thinkpython.com/code/wordlist.py.
#
words = open('words.txt')

def method_one(words):
   wordList = []
   for line in words:
       line = line.strip()
       wordList.append(line)
   print len(wordList)
   print wordList[:10]

# method_one(words)

def method_two(words):
   wordList = []
   for line in words:
       line = line.strip()
       wordList += [line]
   print len(wordList)
   print wordList[:10]

method_two(words)

# To be honest, I couldn't tell the difference between the two runs. I 
# don't know how to tell the system to measure these things at the moment.
# I even added the str.strip() method which seemed to gum things up a bit
# but kept both of them about equal to each other as far as I could tell.
