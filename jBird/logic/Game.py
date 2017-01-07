import pygame


class Game(object):
    def __init__(self):
        self.level = 1
        self.round = 1

    def next_level(self):
        self.level += 1

    def next_round(self):
        self.round = ((self.round + 1) % 3) + 1
