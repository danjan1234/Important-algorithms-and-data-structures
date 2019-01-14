from card import Card, Suit
import numpy as np


class Deck:
    def __init__(self, n_decks=1):
        self._n_decks = n_decks
        self._cards_arr = []

    def generate(self):
        for _ in range(self._n_decks):
            for i in np.random.permutation(13):
                for j in np.random.permutation(4):
                    self._cards_arr.append(Card(i, Suit(j)))

    def remove_card(self):
        if self.size() == 0:
            return
        return self._cards_arr.pop()

    def size(self):
        return len(self._cards_arr)


if __name__ == '__main__':
    deck = Deck(n_decks=1)
    deck.generate()
    pass
