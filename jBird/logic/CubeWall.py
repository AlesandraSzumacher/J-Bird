from jBird.utils.Constants import BoardSize, WallColor


class CubeWallRight:
    """Class containing methods and attributes referring to right wall of the cube."""

    def __init__(self, center_up):
        """Initializing the right wall of the cube."""
        self.center = center_up
        self.coordinates = []
        self.count_coords()
        self.color = WallColor.RIGHT_WALL_COLOR.value

    def count_coords(self):
        """Returns the positions of coords of right walls."""
        up = (self.center[0] + BoardSize.TILE_WIDTH.value // 2, self.center[1])
        r = (self.center[0] + BoardSize.TILE_WIDTH.value // 2,
             self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value // 2)
        down = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value)
        l = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2)

        self.coordinates.append(up)
        self.coordinates.append(r)
        self.coordinates.append(down)
        self.coordinates.append(l)


class CubeWallLeft:
    """Class containing methods and attributes referring to left wall of the cube."""

    def __init__(self, center_up):
        """Initializing the left wall of the cube."""
        self.center = center_up
        self.coordinates = []
        self.count_coords()
        self.color = WallColor.LEFT_WALL_COLOR.value

    def count_coords(self):
        """Returns the positions of coords of left walls."""
        up = (self.center[0] - BoardSize.TILE_WIDTH.value // 2, self.center[1])
        r = (self.center[0] - BoardSize.TILE_WIDTH.value // 2,
             self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value // 2)
        down = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value)
        l = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2)

        self.coordinates.append(up)
        self.coordinates.append(l)
        self.coordinates.append(down)
        self.coordinates.append(r)
