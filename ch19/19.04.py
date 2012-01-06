# For this exercise, you will write an image viewer. Here is a simple
# example:
#
# g = Gui()
# canvas = g.ca(width=300)
# photo = PhotoImage(file='danger.gif')
# canvas.image([0,0], image=photo)
# g.mainloop()
#
# PhotoImage reads a file and returns a PhotoImage object that Tkinter can
# display. Canvas.image puts the image on the canvas, centered on the given
# coordinates. You can also put images on labels, buttons, and some other
# widgets:
#
# g.la(image=photo)
# g.bu(image=photo)
# 
# PhotoImage can only handle a few image formats, like GIF and PPM, but we can
# use the Python Imaging Library (PIL) to read other files.
# The name of the PIL module is Image, but Tkinter defines an object with the 
# same name. To avoid the conflict, you can use import...as like this:
# 
# import Image as PIL
# import ImageTk
# The first line imports Image and gives it the local name PIL. The second line
# imports ImageTk, which can translate a PIL image into a Tkinter PhotoImage. 
# Here’s an example:
#
# image = PIL.open('allen.png')
# photo2 = ImageTk.PhotoImage(image)
# g.la(image=photo2)
#
# 1. Download image_demo.py, danger.gif and allen.png from 
# thinkpython.com/code.
# Run image_demo.py. You might have to install PIL and ImageTk. They are
# probably in your software repository, but if not you can get them from
# pythonware.com/products/pil/.
# 2. In image_demo.py change the name of the second PhotoImage from photo2 to
# photo and run the program again. You should see the second PhotoImage but
# not the first.
# The problem is that when you reassign photo it overwrites the reference to 
# the first PhotoImage, which then disappears. The same thing happens if you
# assign a PhotoImage to a local variable; it disappears when the function
# ends.
# To avoid this problem, you have to store a reference to each PhotoImage you 
# want to keep.
# You can use a global variable, or store PhotoImages in a data structure or as
# an attribute of an object.
# This behavior can be frustrating, which is why I am warning you (and why the
# example image says "Danger!").
# 3. Starting with this example, write a program that takes the name of a 
# directory and loops through all the files, displaying any files that PIL
# recognizes as images. You can use a try statement to catch the files PIL 
# doesn't recognize.
# When the user clicks on the image, the program should display the next one.
# 4. PIL provides a variety of methods for manipulating images. You can read 
# about them at pythonware.com/library/pil/handbook. As a challenge, choose a 
# few of these methods and provide a GUI for applying them to images.
# You can download a simple solution from thinkpython.com/code/ImageBrowser.py.

# Current Status: Incomplete