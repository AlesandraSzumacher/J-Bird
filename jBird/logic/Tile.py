from jBird.utils.Constants import BoardSize
from jBird.utils.LevelsUtils import TilesState



class Tile:
    """Class containing methods and attributes referring to single tile."""
    def __init__(self, centerX, centerY):
        """Initializing the single tile."""
        self.center = (centerX, centerY)
        self.coordinates = []
        self.countCoordinates()
        self.state = TilesState.NOT_TOUCHED

    def countCoordinates(self):
        """Returns the positions of tile's coordinates."""
        self.coordinates.append([self.center[0] - BoardSize.TILE_WIDTH.value // 2,
                                 self.center[1]])
        self.coordinates.append([self.center[0],
                                 self.center[1] - BoardSize.TILE_HEIGHT.value//2])
        self.coordinates.append([self.center[0] + BoardSize.TILE_WIDTH.value//2, self.center[1]])
        self.coordinates.append([self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value//2])

    def pressed(self, mouse):
        """Checking if the Tile is pressed."""
        return self.tileControl.pressed(self.center, mouse)

    def change_state(self, level):
        """Changes state of tile and returns if succeed."""
        if self.state == TilesState.NOT_TOUCHED:
            self.state = TilesState.TOUCHED
            return 1
        if self.state == TilesState.TOUCHED and level > 1:
            self.state = TilesState.DOUBLE_TOUCHED
            return 1
        if self.state == TilesState.DOUBLE_TOUCHED and level == 3:
            self.state = TilesState.TOUCHED
            return -1
        return 0

        # if self.state == TilesState.NOT_TOUCHED.value:
        #     self.state = TilesState.TOUCHED.value
        #     return True
        # return False



