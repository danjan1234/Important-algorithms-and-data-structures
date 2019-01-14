from cards_in_hand import CardsInHand


class Player:
    def __init__(self, player_id):
        self._player_id = player_id
        self._cards_in_hand = CardsInHand()

    def add_card(self, card):
        if card is None:
            return
        self._cards_in_hand.add_card(card)

    def remove_card(self):
        if self._cards_in_hand.n_cards() == 0:
            return
        return self._cards_in_hand.remove_card()

    def n_cards(self):
        return self._cards_in_hand.n_cards()
