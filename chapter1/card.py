import collections

Card = collections.namedtuple('Card', 'rank suit')


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # spades/黑桃 diamonds/方片 clubs/梅花 hearts/红心
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __repr__(self):
        return 'Card {},{}'.format(self.ranks, self.suits)


    def spade_high(self, card):
        suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]


# beer_card = Card('7', 'diamonds')
# print(beer_card)

deck = FrenchDeck()

# 实现__len__
print(len(deck))

# 实现__repr__
print(deck)

# 实现__getitem__
print(deck[:-1])

# for card in deck:
#     print(card)

for card in sorted(deck, key=deck.spade_high):
    print(card)
