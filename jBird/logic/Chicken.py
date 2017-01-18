import pygame

from jBird.utils.ScreenSize import Positions


class Chicken():
    def __init__(self):
        self.position = Positions.CHICKEN_INIT_POSITION.value
        self.direction = "INIT DOWN"
        self.feet_coords = [41, 78]
        self.tile_center = 0

    def move(self, direction, tile):
        print("Kurczak zjezdzasz w dol idioto")
        self.position[1] += 100

    def move_down_tile(self, tile):
        self.position[0] = tile.center[0] - self.feet_coords[0]
        self.position[1] = tile.center[1] - self.feet_coords[1]
        self.tile_center = tile.center

    def move_down(self, center):
        self.position[0] = center[0] - self.feet_coords[0]
        self.position[1] = center[1] - self.feet_coords[1]
        self.tile_center = center
