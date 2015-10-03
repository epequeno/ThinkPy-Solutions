#Exercise 3   Modify the program from the previous exercise to print the 20
# most frequently-used words in the book.

from string import punctuation, whitespace

origin = 'origin.txt'
huck = 'huck.txt'
frank = 'frank.txt'
great = 'great.txt'
meta = 'meta.txt'
sherlock = 'sherlock.txt'
tale = 'tale.txt'

books = [origin, huck, frank, great, meta, sherlock, tale]

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    op = open(book, 'r')
    for line in op:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    op.close()
    return list_
    
  
def clean(word):
     result = ''
     for char in word:
         if (char in whitespace) or (char in punctuation):
             pass
         else:
             result += char.lower()
     return result

def histogram(data):
     hist = {}
     for word in data:
         if word == '':
             pass
         else:
             hist[word] = hist.get(word, 0) + 1
     return hist

def main():
    for book in books:
        data = [clean(word) for word in words(book)]
        print "Stats for %s:" % book
        hist = histogram(data)
        top20 = []
        for key in hist:
            top20.append([hist[key], key])
        top20.sort(reverse=True)
        for i in range(0, 20):
            print "  %s) %s %s" % (i + 1, top20[i][1], top20[i][0])
        
        print "\n"        

main()