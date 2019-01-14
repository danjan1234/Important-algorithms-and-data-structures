"""Abstract state machine class"""
from abc import ABC
from collections import deque


class StateMachine(ABC):
    """Abstract state machine class"""
    def __init__(self, initial_sate):
        self._initial_state = initial_sate
        self._state_queue = deque()

    def run(self):
        self._state_queue.append(self._initial_state)
        while len(self._state_queue) > 0:
            curr_state = self._state_queue.popleft()
            curr_state.run()
            for next_state in curr_state.get_next_states():
                self._state_queue.append(next_state)
