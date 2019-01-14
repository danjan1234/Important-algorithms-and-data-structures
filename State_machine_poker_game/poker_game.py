"""A state machine driven poker game"""
from poker_game_setup import PokerGameSetup
from state_machine import StateMachine
from poker_game_states import *


class PokerGame(StateMachine):
    def __init__(self, n_decks=1, n_players=2):
        self._n_decks = n_decks
        self._n_players = n_players
        self._game = PokerGameSetup(n_decks=self._n_decks, n_players=self._n_players)
        self._initialization_state = Initialization(self._game)
        super().__init__(self._initialization_state)


if __name__ == '__main__':
    game = PokerGame(n_decks=1, n_players=3)
    game.run()
    pass
