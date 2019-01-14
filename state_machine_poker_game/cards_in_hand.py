import random


class CardsInHand:
    def __init__(self):
        self._cards_arr = []
        self._n_cards = 0

    def add_card(self, card):
        if card is None:
            return
        self._cards_arr.append(card)
        self._n_cards += 1

    def remove_card(self):
        if self._n_cards == 0:
            return
        index = 0
        while self._cards_arr[index] is None:
            index = random.randint(0, len(self._cards_arr) - 1)
        rtn = self._cards_arr[index]
        self._cards_arr[index] = None
        self._n_cards -= 1
        return rtn

    def n_cards(self):
        return self._n_cards
