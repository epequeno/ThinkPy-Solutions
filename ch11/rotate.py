def normalize(x):
    if x > 122:
        while x > 122:
            x -= 26
    elif x < 97:
        while x < 97:
            x += 26
    return x
    
def rotate_word(word, amount):
    new_word = ''
    for letter in word:
        letter = letter.lower()
        if ord(letter) + amount > 122:
            new_word += chr(normalize(ord(letter) + amount))
        elif ord(letter) + amount < 97:
            new_word += chr(normalize(ord(letter) + amount))
        else:
            new_word += chr(ord(letter) + amount)
    return new_word
