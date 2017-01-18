import pygame

from jBird.utils.ScreenSize import Positions


class Chicken():
    def __init__(self):
        self.position = Positions.CHICKEN_INIT_POSITION.value
        self.level = -1
        self.feet_coords = [41, 78]
        self.tile_center = 0

        self.prev_level = -1
        self.prev_tile_center = 0
        self.prev_position =  Positions.CHICKEN_INIT_POSITION.value

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

    def save_prev_position(self):
        self.prev_level = self.level
        self.prev_position = self.position
        self.prev_tile_center = self.tile_center

    def reset_change(self):
         self.level = self.prev_level
         self.position = self.prev_position
         self.tile_center = self.prev_tile_center

