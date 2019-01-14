"""Game setup"""
import random

from deck import Deck
from discarded_cards import DiscardedCards
from player import Player


class PokerGameSetup:
    def __init__(self, n_decks=1, n_players=2):
        self._n_decks = n_decks
        self._n_players = n_players
        self._deck = Deck(n_decks=self._n_decks)
        self._discarded_cards = DiscardedCards()
        self._players = []
        for i in range(self._n_players):
            self._players.append(Player(i))
        self._curr_player_id = 0

    def start_game(self):
        print("Start the game ...")
        self._deck.generate()

    def distribute_cards(self):
        print("Distribute cards ...")
        while self._deck.size() > 0:
            if self._curr_player_id == self._n_players:
                self._curr_player_id = 0
            card = self._deck.remove_card()
            self._players[self._curr_player_id].add_card(card)
            self._curr_player_id += 1

    def play(self):
        if self._curr_player_id == self._n_players:
            self._curr_player_id = 0
        card = self._players[self._curr_player_id].remove_card()
        print("Player {} has offered one card {}".format(self._curr_player_id, card))
        self._discarded_cards.add_card(card)
        self._curr_player_id += 1

    def check_win(self, force_win=False):
        if random.randint(0, 100) == 3:
            force_win = True
        return force_win

    def has_won(self):
        print("Player {} has won".format(self._curr_player_id))

    def no_more_cards(self):
        if sum([player.n_cards() for player in self._players]) == 0:
            print("No more cards to play")
            return True
        else:
            return False

    def exit_game(self):
        print("Exit the game ...")
