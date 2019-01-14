"""Class of cards"""
from enum import Enum


class Suit(Enum):
    DIAMOND = 0
    HEART = 1
    SPADE = 2
    CLUB = 3


class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return "{}-{}".format(self.number, self.suit.name)
