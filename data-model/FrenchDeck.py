import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == "__main__":
    french_deck = FrenchDeck()
    print(french_deck.ranks)
    print(french_deck.suits)
    print(len(french_deck))
    print(french_deck[-1])
    print(french_deck[:3])
    print(french_deck[12::13])
    print(choice(french_deck))
    for card in french_deck:
        print(card)
    for card in reversed(french_deck):
        print(card)

    for card in sorted(french_deck, key=spades_high):  # doctest: +ELLIPSIS
        print(card)

