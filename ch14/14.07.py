# The Internet Movie Database (IMDb) is an online collection of information
# about movies. Their database is available in plain text format, so it is
# reasonably easy to read from Python.
# For this exercise, the files you need are actors.list.gz and 
# actresses.list.gz; you can download them from 
# www.imdb.com/interfaces#plain.
# I have written a program that parses these files and splits them into actor
# names, movie titles, etc.
# You can download it from thinkpython.com/code/imdb.py.
# If you run imdb.py as a script, it reads actors.list.gz and prints one 
# actor-movie pair per line.
# Or, if you import imdb you can use the function process_file to, well, 
# process the file. The arguments are a filename, a function object and an 
# optional number of lines to process. Here is an example:
#
# import imdb
# def print_info(actor, date, title, role):
#     print actor, date, title, role
# imdb.process_file('actors.list.gz', print_info)
#
# When you call process_file, it opens filename, reads the contents, and calls
# print_info once for each line in the file. print_info takes an actor, date,
# movie title and role as arguments and prints them.
# 1. Write a program that reads actors.list.gz and actresses.list.gz and uses
# shelve to build a database that maps from each actor to a list of his or her
# films.
# 2. Two actors are "costars" if they have been in at least one movie together.
# Process the database you built in the previous step and build a second
# database that maps from each actor to a list of his or her costars.
# 3. Write a program that can play the "Six Degrees of Kevin Bacon," which you
# can read about at
# wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon. 
# This problem is challenging because it requires you to find the shortest
# path in a graph. You can read about shortest path algorithms at 
# wikipedia.org/wiki/Shortest_path_problem.

# Current Status: Incomplete