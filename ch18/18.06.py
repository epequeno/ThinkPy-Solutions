# This exercise uses TurtleWorld from Chapter 4. You will write code that
# makes Turtles play tag. If you are not familiar with the rules of tag, see
# wikipedia.org/wiki/Tag_(game).
# 1. Download thinkpython.com/code/Wobbler.py and run it. You should see a
# TurtleWorld with three Turtles. If you press the Run button, the Turtles
# wander at random.
# 2. Read the code and make sure you understand how it works. The Wobbler class
# inherits from Turtle, which means that the Turtle methods lt, rt, fd and bk
# work on Wobblers. The step method gets invoked by TurtleWorld. It invokes
# steer, which turns the Turtle in the desired direction, wobble, which makes
# a random turn in proportion to the Turtle's clumsiness, and move, which moves 
# forward a few pixels, depending on the Turtle’s speed.
# 3. Create a file named Tagger.py. Import everything from Wobbler, then 
# define a class named Tagger that inherits from Wobbler. Call make_world
# passing the Tagger class object as an argument.
# 4. Add a steer method to Tagger to override the one in Wobbler. As a 
# starting place, write a version that always points the Turtle toward the
# origin. Hint: use the math function atan2 and the Turtle attributes x, y 
# and heading.
# 5. Modify steer so that the Turtles stay in bounds. For debugging, you might
# want to use the Step button, which invokes step once on each Turtle.
# 6. Modify steer so that each Turtle points toward its nearest neighbor. 
# Hint: Turtles have an attribute, world, that is a reference to the
# TurtleWorld they live in, and the TurtleWorld has an attribute, animals, 
# that is a list of all Turtles in the world.
# 7. Modify steer so the Turtles play tag. You can add methods to Tagger and
# you can override steer and __init__, but you may not modify or override step,
# wobble or move. Also, steer is allowed to change the heading of the Turtle 
# but not the position. Adjust the rules and your steer method for good 
# quality play; for example, it should be possible for the slow Turtle to tag 
# the faster Turtles eventually. You can get my solution from 
# thinkpython.com/code/Tagger.py.

