import pygame
from pygame import gfxdraw

from jBird.utils.ScreenSize import TileColor


class Rhombus:
    def __init__(self, tile):
        self.tile = tile
        self.listOfCoordinates = tile.coordinates
        self.color = TileColor.START_COLOR.value

    def draw_rhombus(self, screen):
        print(self.color)
        pygame.gfxdraw.filled_polygon(screen, self.listOfCoordinates, self.color)

        return screen

    def changeColor(self, color):
        self.color = color
        # print(self.color)
        # pygame.gfxdraw.filled_polygon(screen, self.listOfCoordinates, color)
