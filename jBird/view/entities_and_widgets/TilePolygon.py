import pygame
from pygame import gfxdraw

from jBird.utils.Constants import TileColor


class TilePolygon:
    def __init__(self, tile, color=TileColor.START_COLOR.value):
        self.tile = tile
        self.list_of_coordinates = tile.coordinates
        self.color = color

    def draw_rhombus(self, screen):
        pygame.gfxdraw.filled_polygon(screen, self.list_of_coordinates, self.color)

        return screen

    def change_color(self, color):
        self.color = color
