# Visual is a Python module that provides 3-D graphics. It is not always 
# included in a Python installation, so you might have to install it from your
# software repository or, if it’s not there, from vpython.org.
# The following example creates a 3-D space that is 256 units wide, long and 
# high, and sets the “center” to be the point (128, 128, 128). Then it draws
# a blue sphere.
#
# from visual import *
# scene.range = (256, 256, 256)
# scene.center = (128, 128, 128)
# color = (0.1, 0.1, 0.9)  # mostly blue
# sphere(pos=scene.center, radius=128, color=color)
#
# color is an RGB tuple; that is, the elements are Red-Green-Blue levels 
# between 0.0 and 1.0 (see wikipedia.org/wiki/RGB_color_model).
# If you run this code, you should see a window with a black background and a
# blue sphere. If you drag the middle button up and down, you can zoom in and
# out. You can also rotate the scene by dragging the right button, but with
# only one sphere in the world, it is hard to tell the difference.
# The following loop creates a cube of spheres:
#
# t = range(0, 256, 51)
# for x in t:
# for y in t:
# for z in t:
# pos = x, y, z
# sphere(pos=pos, radius=10, color=color)
#
# 1. Put this code in a script and make sure it works for you.
# 2. Modify the program so that each sphere in the cube has the color that
# corresponds to its position in RGB space. Notice that the coordinates are
# in the range 0–255, but the RGB tuples are in the range 0.0–1.0.
# 3. Download thinkpython.com/code/color_list.py and use the function
# read_colors to generate a list of the available colors on your system,
# their names and RGB values. For each named color draw a sphere in the 
# position that corresponds to its RGB values. You can see my solution at 
# thinkpython.com/code/color_space.py.

# Current Status: Incomplete