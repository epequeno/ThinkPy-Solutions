# Write a Deck method named sort that uses the list method sort to sort the
# cards in a Deck. sort uses the __cmp__ method we defined to determine sort
# order.

# Current Status: Incomplete

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

class Deck(object):
  def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
  def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)



deck = Deck()
deck.sort()
