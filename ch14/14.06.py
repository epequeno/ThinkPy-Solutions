# In a large collection of MP3 files, there may be more than one copy of the
# same song, stored in different directories or with different file names. The
# goal of this exercise is to search for these duplicates.
# 1. Write a program that searches a directory and all of its subdirectories,
# recursively, and returns a list of complete paths for all files with a given 
# suffix (like .mp3). Hint: os.path provides several useful functions for
# manipulating file and path names.
# 2. To recognize duplicates, you can use a hash function that reads the file
# and generates a short summary of the contents. For example, MD5 
# (Message-Digest algorithm 5) takes an arbitrarily-long "message" and returns
# a 128-bit "checksum." The probability is very small that two files with
# different contents will return the same checksum.
# You can read about MD5 at wikipedia.org/wiki/Md5. On a Unix system you can
# use the program md5sum and a pipe to compute checksums from Python.

