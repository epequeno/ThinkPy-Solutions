# Move the function call back to the bottom and move the definition of
# print_lyrics after the definition of repeat_lyrics. What happens when 
# you run this program?

# Current Status: Complete

def repeat_lyrics():
   print_lyrics()
   print_lyrics()

def print_lyrics():
   print "I'm a lumberjack, and I'm okay."
   print "I sleep all night and I work all day."

repeat_lyrics()

# Even though print_lyrics() hasn't been defined, repeat_lyrics() can still
# call for it. This function works the same as having repeat_lyrics() come 
# after print_lyrics()