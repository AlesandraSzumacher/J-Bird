import pygame
from jBird.utils.ScreenSize import PlayerPos

class Player(object):
    def __init__(self, nick):
        self.nick = nick
        self.hp = 2
        self.points = 0
        self.width = PlayerPos.START_WIDTH.value
        self.height = PlayerPos.START_HEIGHT.value

    def sub_hp(self):
        self.hp -= 1

    def add_points(self, points):
        self.points += points

    def add_hp(self):
        self.hp += 1

    def did_i_lose(self):
        if self.hp < 0:
            return True
        return False
