import os

import pygame


class SnakeImage:
    def __init__(self):
        """Loads new snake in ball"""
        self.folder = os.path.dirname(os.path.realpath(__file__))
        self.image = pygame.image.load(os.path.join(self.folder, "snakeBall.PNG"))

    def change_ball_into_snake(self):
        """Changes image with big ball to snake"""
        self.image = pygame.image.load(os.path.join(self.folder, "waz.png"))
