# Write a Deck method named sort that uses the list method sort to sort the
# cards in a Deck. sort uses the __cmp__ method we defined to determine sort
# order.

# Current Status: Complete

from random import shuffle

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])
    
    def __repr__(self):
        return 'Card <{}, {}>'.format(self.rank_names[self.rank], self.suit_names[self.suit])
    
    # I'm using the following 'rich comparison' methods in place of __cmp__ 
    # https://docs.python.org/2/reference/datamodel.html#object.__lt__
    
    def __lt__(self, other):
        return self.rank < other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __eq__(self, other):
        return self.rank == other.rank



class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]
        
    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])
    
    def __repr__(self):
        return "Deck <{}>".format(self.cards)
    
    def __len__(self):
        return len(self.cards)
    
    def shuffle(self):
        shuffle(self.cards)
        return "deck has been shuffled."
    
    def sort(self):
        self.cards.sort()
        return "deck has been sorted."
    



deck = Deck()
deck.shuffle()
deck
deck.sort()
print(deck)
