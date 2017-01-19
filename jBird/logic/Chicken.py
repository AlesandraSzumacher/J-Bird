import pygame

from jBird.utils.ScreenSize import Positions


class Chicken():
    def __init__(self):
        self.position = Positions.CHICKEN_INIT_POSITION.value
        self.level = -1
        self.feet_coords = (41, 78)
        self.tile_center = Positions.CHICKEN_INIT_POSITION.value
        self.prev_tile_center = Positions.CHICKEN_INIT_POSITION.value
        self.prev_level = -1
        self.prev_position = Positions.CHICKEN_INIT_POSITION.value

    def setTileCenter(self, center):
        self.tile_center = center
        self.setPosition()

    def setPosition(self):
        self.position[0] = self.tile_center[0] - self.feet_coords[0]
        self.position[1] = self.tile_center[1] - self.feet_coords[1]











    def move_down_tile(self, tile):
        self.position[0] = tile.center[0] - self.feet_coords[0]
        self.position[1] = tile.center[1] - self.feet_coords[1]
        self.tile_center = tile.center

    def move(self, center):
        self.save_prev_position()

        self.position[0] = center[0] - self.feet_coords[0]
        self.position[1] = center[1] - self.feet_coords[1]

        self.tile_center = center

    def save_prev_position(self):
        print("save poss")
        print(self.level, " ", " ", self.tile_center)

        self.prev_level = self.level
        self.prev_position[0] = self.position[0]
        self.prev_position[1] = self.position[1]

        self.prev_tile_center[0] = self.tile_center[0]
        self.prev_tile_center[1] = self.tile_center[1]
        print( self.prev_level, " ", " ", self.prev_tile_center)


    def reset_change(self):
        #print(self.level, " ", self.position, " ", self.tile_center)
        #print( self.prev_level, " ", self.prev_position, " ", self.prev_tile_center)
        self.level = self.prev_level
        self.position = self.prev_position
        self.tile_center = self.prev_tile_center
        # print(self.level, " ", self.position, " ", self.tile_center)


    def getPosition(self):
        return self.position