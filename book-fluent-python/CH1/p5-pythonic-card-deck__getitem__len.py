# implementation of special methods with FrenchDeck class.
# i.e. __getitem__ enables to class to use [] operator.
# Set CONFIG_ENABLE_GETITEM or CONFIG_ENABLE_LEN to 0 and see what happens if you do not
# implement get item.

import collections
from random import choice 

Card=collections.namedtuple('Card',['rank','suit'])

CONFIG_ENABLE_GETITEM=1
CONFIG_ENABLE_LEN=1

class FrenchDeck:
    ranks=[str(n) for n in range(2,11)] + list('JQKA')
    suits='spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    if CONFIG_ENABLE_LEN:
        def __len__(self):
            return len(self._cards)

    if CONFIG_ENABLE_GETITEM:
        def __getitem__(self, position):
            return self._cards[position]

    def __repr__(self):
        return "FrenchDeck class object"

beer_card=Card('7','diamons')
print(beer_card)

deck=FrenchDeck()
print(len(deck))
print(deck)
quit(0)

print(deck[0])
print(deck[-1])

print(deck)
for i in range(0,3):
    print(choice(deck))

print(deck[:3])
print(deck[12:13])
print(deck[::3])

for card in deck:
    print(card)

print('-' * 50)
print(Card('Q', 'hearts') in deck)
print(Card('7', 'hearst') in deck)

suit_values=dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
