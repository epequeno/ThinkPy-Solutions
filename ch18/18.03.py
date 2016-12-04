# Write a Deck method called deal_hands that takes two parameters, the number
# of hands and the number of cards per hand, and that creates new Hand
# objects, deals the appropriate number of cards per hand, and returns a 
# list of Hand objects.
# Inheritance is a useful feature. Some programs that would be repetitive
# without inheritance can be written more elegantly with it. Inheritance can
# facilitate code reuse, since you can customize the behavior of parent
# classes without having to modify them. In some cases, the inheritance 
# structure reflects the natural structure of the problem, which makes the
# program easier to understand.
# On the other hand, inheritance can make programs difficult to read. When
# a method is invoked, it is sometimes not clear where to find its definition.
# The relevant code may be scattered among several modules. Also, many of 
# the things that can be done using inheritance can be done as well or 
# better without it.

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
    
    def deal_hands(self, num_of_hands, cards_per_hand):
        if (num_of_hands * cards_per_hand) > len(self):
            msg = '\n{} hands with {} cards each is {} cards\
            \nTotal cards left in deck: {}'.format(num_of_hands, cards_per_hand, num_of_hands * cards_per_hand, len(self))
            raise ValueError(msg)
        else:
            hands = []
            for h in range(num_of_hands):
                hand = Hand()
                for c in range(cards_per_hand):
                    hand.cards.append(self.cards.pop())
                hands.append(hand)
            return hands
            
                    
    
class Hand(object):
    def __init__(self):
        self.cards = []
        
    def __repr__(self):
        return "Hand <{}>".format(self.cards)