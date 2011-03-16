word = raw_input('Word?\n')

def right_justify(s):
   print " " * (70 - len(word)) + word

right_justify(word)
