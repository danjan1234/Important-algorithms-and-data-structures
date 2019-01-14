"""Abstract State class"""
from abc import ABC, abstractmethod


class State(ABC):
    """Abstract state class"""
    def __init__(self, game):
        self._game_setup = game

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def get_next_states(self):
        pass
