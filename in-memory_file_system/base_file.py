"""A base file abstract class"""
from abc import ABC

import time


class BaseFile(ABC):
    """A base file abstract class"""
    def __init__(self, name, created_time=None, size=None):
        self._name = name
        self._created_time = created_time if created_time is not None else time.time()
        self._size = size if size is not None else 0
        self._parent = None     # A pointer to the parent directory

    def print(self):
        return self._name

    def get_full_path(self):
        paths = []
        curr = self
        while curr is not None:
            paths.append(curr.name)
            curr = curr._parent
        return "/".join(paths[::-1])
