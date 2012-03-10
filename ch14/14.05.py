# The urllib module provides methods for manipulating URLs and downloading
# information from the web. The following example downloads and prints a 
# secret message from thinkpython.com:
# import urllib
# conn = urllib.urlopen('http://thinkpython.com/secret.html')
# for line in conn.fp:
# print line.strip()
# Run this code and follow the instructions you see there.

# Current Status: Incomplete

#import urllib
#
#conn = urllib.urlopen('http://thinkpython.com/secret.html')
#
#for line in conn.fp:
#    print line.strip()

# If you are reading this, you are probably working on the urllib exercise
# from Think Python.

# Next, you should read the documentation of the urllib module at
# http://docs.python.org/lib/module-urllib.html

# Then go to www.uszip.com, which provides information about every zip code
# in the country.  For example, the URL
# http://www.uszip.com/zip/02492
# provides information about Needham MA, including population, longitude
# and latitude, etc.

# Write a program that prompts the user for a zip code and prints the
# name and population of the corresponding town.

# Note: the text you get from uszip.com is in HTML, the language most web pages
# are written in.  Even if you don't know HTML, you should be able to extract
# the information you are looking for.

# By the way, your program is an example of a "screen scraper."  You can
# read more about this term at
# http://wikipedia.org/wiki/Screen_scraping

# Sites that make money from advertising don't like screen scrapers
# because they don't display the ads.  Using a screen scraper violates
# the terms of service for some sites; that's why this is a secret
# exercise!

# Current Status: Complete

import requests
import re

user_input = str(raw_input("Zip Code? "))

def is_len_valid(user_input):
    return len(user_input) == 5
        
def is_all_num(user_input):
    flag = True
    for char in user_input:
        if char.isdigit() == False:
            flag = False
            return flag
    return flag

def is_query_valid(data):
    return "<title>" in data_list[1]

def main():
    if is_len_valid(user_input) == False:
        print "The input must have 5 digits"
    elif is_all_num(user_input) == False:
        print "Zip Codes don't have letters!"
    elif is_query_valid(data) == False:
        print "Information for %s not found." % user_input
    else:
        city = re.findall(r'\<title\>Zip\ code\ for\ (.*?)\ -\ ', data)
        population = re.findall(r'Population:\<\/b\>\<\/td\>\<td\>(.*?)\ \<span', data)
        print "%s (%s) has a population of %s" % (city[0], user_input, population[0])

data = requests.get("http://www.uszip.com/zip/" + user_input).content
data_list = [line for line in data.splitlines()]
main()