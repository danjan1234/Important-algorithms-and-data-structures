class DiscardedCards:
    def __init__(self):
        self._card_arr = []

    def add_card(self, card):
        if card is None:
            return
        self._card_arr.append(card)
