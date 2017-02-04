from jBird.utils.Constants import BoardSize
from jBird.utils.LevelsUtils import TilesState



class Tile:
    """Class containing methods and attributes referring to single tile."""
    def __init__(self, centerX, centerY):
        """Initializing the single tile."""
        self.center = [centerX, centerY]
        self.coordinates = []
        self.countCoordinates()
        self.state = TilesState.NOT_TOUCHED.value

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

    def change_state(self):
        if self.state == TilesState.NOT_TOUCHED.value:
            self.state = TilesState.TOUCHED.value



