from jBird.logic.CubeWall import CubeWallLeft, CubeWallRight
from jBird.logic.Tile import Tile
from jBird.utils.Constants import BoardSize


class Board:
    """Class containing methods and attributes referring to game board."""
    def __init__(self, firstCenter):
        """Board initializing."""
        self.listOfTiles = []
        self.listOfCubeWalls = []
        self.addTile(firstCenter, 0)
        self.numberOfTouchTiles = 0

    def addTile(self, firstCenter, level):
        """Setting the Tiles on the board."""
        self.listOfTiles.append(Tile(firstCenter[0], firstCenter[1]))
        self.listOfCubeWalls.append(CubeWallLeft(firstCenter))
        self.listOfCubeWalls.append(CubeWallRight(firstCenter))

        leftNextCenter = [firstCenter[0] - BoardSize.TILE_WIDTH.value // 2,
                          firstCenter[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        rightNextCenter = [firstCenter[0] + BoardSize.TILE_WIDTH.value // 2,
                           firstCenter[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]

        if level == (BoardSize.LEVELS_NUMBER.value - 1):
            return

        self.addTile(leftNextCenter, level + 1)
        self.addTile(rightNextCenter, level + 1)

    def returnListOfTiles(self):
        """returns the list of Tiles(to get their positions)."""
        return self.listOfTiles


    def countNextUpTiles(self, center):
        """Gets the position of Tiles up."""
        leftNextCenter = [center[0] - BoardSize.TILE_WIDTH.value // 2,
                          center[1] - BoardSize.TILE_HEIGHT.value // 2 - BoardSize.CUBE_BREAK_HEIGHT.value]
        rightNextCenter = [center[0] + BoardSize.TILE_WIDTH.value // 2,
                           center[1] - BoardSize.TILE_HEIGHT.value // 2 - BoardSize.CUBE_BREAK_HEIGHT.value]
        return (leftNextCenter, rightNextCenter)


    def countTwoDownTiles(self, center):
        """Gets the position of two down Tiles."""
        leftNextCenter = [center[0] - BoardSize.TILE_WIDTH.value // 2,
                          center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        rightNextCenter = [center[0] + BoardSize.TILE_WIDTH.value // 2,
                           center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        return (leftNextCenter, rightNextCenter)

    def if_tile_is_in_board(self, center):
        """Checks if the Tile is present on the board."""
        for tile in self.listOfTiles:
            if tile.center[0] == center[0] and tile.center[1] == center[1]:
                return True
        return False

    def return_tile_from_board(self, center):
        """Returns Tile by the information about it's center."""
        for tile in self.listOfTiles:
            if tile.center[0] == center[0] and tile.center[1] == center[1]:
                return tile
        return None

