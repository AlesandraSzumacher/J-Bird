import pygame


class Player(object):
    def __init__(self, nick):
        self.nick = nick
        self.hp = 2
        self.points = 0

    def sub_hp(self):
        self.hp -= 1

    def add_points(self, points):
        self.points += points

    def add_hp(self):
        self.hp += 1
