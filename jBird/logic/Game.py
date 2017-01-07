import pygame


class Game(object):
    """Class containing  methods which refer to game, such as levels and rounds."""
    def __init__(self):
        """Initializing new Game."""
        self.level = 1
        self.round = 1

    def next_level(self):
        """Changing level into next."""
        self.level += 1

    def next_round(self):
        """Changing round into next or into first in the new level."""
        self.round = ((self.round + 1) % 3) + 1
