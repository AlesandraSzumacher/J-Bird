from jBird.logic.Tile import Tile
from jBird.utils.ScreenSize import BoardSize


class Board:
    def __init__(self, firstCenter):
        self.listOfTiles = []
        self.addTile(firstCenter, 0)

    def addTile(self, firstCenter, level):
        self.listOfTiles.append(Tile(firstCenter[0], firstCenter[1]))
        leftNextCenter = [firstCenter[0] - BoardSize.TILE_WIDTH.value // 2 , firstCenter[1] + BoardSize.TILE_HEIGHT.value//2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        rightNextCenter = [firstCenter[0] + BoardSize.TILE_WIDTH.value // 2 , firstCenter[1] + BoardSize.TILE_HEIGHT.value//2 + BoardSize.CUBE_BREAK_HEIGHT.value]

        if level == (BoardSize.LEVELS_NUMBER.value - 1):
            return

        self.addTile(leftNextCenter, level + 1)
        self.addTile(rightNextCenter, level + 1)

    def returnListOfTiles(self):
        return self.listOfTiles

Board([601, 100])





