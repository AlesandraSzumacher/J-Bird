from jBird.control.TileControl import TileControl
from jBird.utils.ScreenSize import BoardSize


class Tile:
    def __init__(self, centerX, centerY):
        self.center = [centerX, centerY]
        self.coordinates = []
        self.countCoordinates()
        self.tileControl = TileControl()

    def countCoordinates(self):
        self.coordinates.append([self.center[0] - BoardSize.TILE_WIDTH.value // 2,
                                 self.center[1]])
        self.coordinates.append([self.center[0],
                                 self.center[1] - BoardSize.TILE_HEIGHT.value//2])
        self.coordinates.append([self.center[0] + BoardSize.TILE_WIDTH.value//2, self.center[1]])
        self.coordinates.append([self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value//2])

    def pressed(self, mouse):
        return self.tileControl.pressed(self.center, mouse)

