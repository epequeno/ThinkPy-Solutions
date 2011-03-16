import string

word = str(raw_input('Which word?\n'))
shift = int(raw_input('Shift by how much?\n'))

def rotate_word(word, shift):
   for letter in word:
       word = word.replace(letter, chr(ord(letter) + shift))
   print word

rotate_word(word, shift)
