# Write a program that reads words.txt and prints only the words with 
# more than 20 characters (not counting whitespace).

# Current Status: Complete

wordList = open('words.txt')

def words(word):
    wordCount = 0
    lineCount = 0
    for word in wordList:
        if len(word) > 20:
            print word.rstrip('\r\n')
            wordCount += 1
        lineCount += 1
    percent  = (float(wordCount) / float(lineCount)) * 100.0
    print "%0.3f" % percent + "%"

words(wordList)