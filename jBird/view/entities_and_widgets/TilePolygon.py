import pygame
from pygame import gfxdraw

from jBird.utils.Constants import TileColor


class TilePolygon:
    """Class containing methods and attributes referring to tile - polygon."""

    def __init__(self, tile, color=TileColor.START_COLOR.value):
        """Initialization of single tile polygon."""
        self.tile = tile
        self.list_of_coordinates = tile.coordinates
        self.color = color

    def draw_rhombus(self, screen):
        """Drawing tile which shape is rhombus."""
        pygame.gfxdraw.filled_polygon(screen, self.list_of_coordinates, self.color)

        return screen

    def change_color(self, color):
        """Changing color of tile."""
        self.color = color
