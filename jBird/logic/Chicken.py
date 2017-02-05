import pygame

from jBird.utils.Constants import Positions


class Chicken():
    """Class containing methods and attributes referring to chicken moving on the board."""
    def __init__(self):
        """"Initialization of chicken."""
        self.position = list(Positions.CHICKEN_INIT_POSITION.value)
        self.level = -1
        self.feet_coords = (41, 78)
        self.tile_center = Positions.CHICKEN_INIT_POSITION.value

    def setTileCenter(self, center):
        """Setting the chicken on the center of the tile."""
        if self.tile_center[1] > center[1]:
            self.level += 1
        if self.tile_center[1] < center[1]:
            self.level -= 1

        self.tile_center = center
        self.setPosition()

    def setPosition(self):
        """Setting chicken position."""
        self.position[0] = self.tile_center[0] - self.feet_coords[0]
        self.position[1] = self.tile_center[1] - self.feet_coords[1]

    def getPosition(self):
        """Getting chicken position."""
        return self.position

    def move_to_start_position(self):
        """Moving the chocken back to start position - when die or win a level."""
        self.position = [570, 10]
        self.level = -1
        self.tile_center = [570, 10]
