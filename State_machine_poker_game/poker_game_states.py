"""Poker game states. Note all states are singletons"""
from state import State


class Initialization(State):
    _shared_states = {}

    def __init__(self, game_setup):
        self.__dict__ = self._shared_states
        self._game_setup = game_setup
        super().__init__(self._game_setup)

    def run(self):
        self._game_setup.start_game()
        self._game_setup.distribute_cards()

    def get_next_states(self):
        return [Idle(self._game_setup)]


class Idle(State):
    _shared_states = {}

    def __init__(self, game_setup):
        self.__dict__ = self._shared_states
        self._game_setup = game_setup
        super().__init__(self._game_setup)

    def run(self):
        pass

    def get_next_states(self):
        if self._game_setup.check_win():
            return [Win(self._game_setup)]
        if self._game_setup.no_more_cards():
            return [Exit(self._game_setup)]
        return [Play(self._game_setup)]


class Play(State):
    _shared_states = {}

    def __init__(self, game_setup):
        self.__dict__ = self._shared_states
        self._game_setup = game_setup
        super().__init__(self._game_setup)

    def run(self):
        self._game_setup.play()

    def get_next_states(self):
        return [Idle(self._game_setup)]


class Win(State):
    _shared_states = {}

    def __init__(self, game_setup):
        self.__dict__ = self._shared_states
        self._game_setup = game_setup
        super().__init__(self._game_setup)

    def run(self):
        self._game_setup.has_won()

    def get_next_states(self):
        return [Exit(self._game_setup)]


class Exit(State):
    _shared_states = {}

    def __init__(self, game_setup):
        self.__dict__ = self._shared_states
        self._game_setup = game_setup
        super().__init__(self._game_setup)

    def run(self):
        self._game_setup.exit_game()

    def get_next_states(self):
        return []
