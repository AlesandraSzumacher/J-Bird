from jBird.logic.CubeWall import CubeWallLeft, CubeWallRight
from jBird.logic.Tile import Tile
from jBird.utils.Constants import BoardSize


class Board:
    """Class containing methods and attributes referring to game board."""
    def __init__(self, firstCenter, number_of_levels):
        """Board initializing."""
        self.list_of_tiles = []
        self.list_of_cube_walls = []
        self.number_of_levels = number_of_levels
        self.add_tile(firstCenter, 0)
        self.number_of_touched_tiles = 0

    def add_tile(self, first_center, level):
        """Setting the Tiles on the board."""
        is_in_list = False
        for t in self.list_of_tiles:
            if t.center[0] == first_center[0] and t.center[1] == first_center[1]:
                is_in_list = True

        if not is_in_list:
            self.list_of_tiles.append(Tile(first_center[0], first_center[1]))

        self.list_of_cube_walls.append(CubeWallLeft(first_center))
        self.list_of_cube_walls.append(CubeWallRight(first_center))

        left_next_center = [first_center[0] - BoardSize.TILE_WIDTH.value // 2,
                          first_center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        right_next_center = [first_center[0] + BoardSize.TILE_WIDTH.value // 2,
                           first_center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]

        if (self.number_of_levels - 1) == level:
            return

        self.add_tile(left_next_center, level + 1)
        self.add_tile(right_next_center, level + 1)

    def return_list_of_tiles(self):
        """returns the list of Tiles(to get their positions)."""
        return self.list_of_tiles

    def count_next_up_tiles(self, center):
        """Gets the position of Tiles up."""
        left_next_center = [center[0] - BoardSize.TILE_WIDTH.value // 2,
                          center[1] - BoardSize.TILE_HEIGHT.value // 2 - BoardSize.CUBE_BREAK_HEIGHT.value]
        right_next_center = [center[0] + BoardSize.TILE_WIDTH.value // 2,
                           center[1] - BoardSize.TILE_HEIGHT.value // 2 - BoardSize.CUBE_BREAK_HEIGHT.value]
        return left_next_center, right_next_center


    def count_two_down_tiles(self, center):
        """Gets the position of two down Tiles."""
        leftNextCenter = [center[0] - BoardSize.TILE_WIDTH.value // 2,
                          center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        rightNextCenter = [center[0] + BoardSize.TILE_WIDTH.value // 2,
                           center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value]
        return (leftNextCenter, rightNextCenter)

    def if_tile_is_in_board(self, center):
        """Checks if the Tile is present on the board."""
        for tile in self.list_of_tiles:
            if tile.center[0] == center[0] and tile.center[1] == center[1]:
                return True
        return False

    def return_tile_from_board(self, center):
        """Returns Tile by the information about it's center."""
        for tile in self.list_of_tiles:
            if tile.center[0] == center[0] and tile.center[1] == center[1]:
                return tile
        return None

    def increase_number_of_touched_tiles(self):
        """Increasing the number of tiles which were touched."""
        self.number_of_touched_tiles += 1

    def decrease_number_of_touched_tiles(self):
        """Decreasing the number of tiles which were touched."""
        self.number_of_touched_tiles -= 1
