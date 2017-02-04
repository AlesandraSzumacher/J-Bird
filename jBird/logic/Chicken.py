import pygame

from jBird.utils.Constants import Positions


class Chicken():
    def __init__(self):
        self.position = Positions.CHICKEN_INIT_POSITION.value
        self.level = -1
        self.feet_coords = (41, 78)
        self.tile_center = Positions.CHICKEN_INIT_POSITION.value

    def setTileCenter(self, center):
        if self.tile_center[1] > center[1]:
            self.level += 1
        if self.tile_center[1] < center[1]:
            self.level -= 1

        self.tile_center = center
        self.setPosition()

    def setPosition(self):
        self.position[0] = self.tile_center[0] - self.feet_coords[0]
        self.position[1] = self.tile_center[1] - self.feet_coords[1]

    def getPosition(self):
        return self.position