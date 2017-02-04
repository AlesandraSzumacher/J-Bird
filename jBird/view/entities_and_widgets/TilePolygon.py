import pygame
from pygame import gfxdraw

from jBird.utils.Constants import TileColor


class TilePolygon:
    def __init__(self, tile, color=TileColor.START_COLOR.value):
        self.tile = tile
        self.listOfCoordinates = tile.coordinates
        self.color = color

    def draw_rhombus(self, screen):
        # print(self.color)
        pygame.gfxdraw.filled_polygon(screen, self.listOfCoordinates, self.color)

        return screen

    def changeColor(self, color):
        self.color = color
        # print(self.color)
        # pygame.gfxdraw.filled_polygon(screen, self.listOfCoordinates, color)
