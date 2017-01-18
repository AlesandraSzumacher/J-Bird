from jBird.utils.ScreenSize import BoardSize, WallColor


class CubeWallRight:
    def __init__(self, centerUp):
        self.center = centerUp
        self.coordinates = []
        self.countCoords()
        self.color = WallColor.RIGHT_WALL_COLOR.value

    def countCoords(self):
        up = (self.center[0] + BoardSize.TILE_WIDTH.value // 2, self.center[1])
        r = (self.center[0] + BoardSize.TILE_WIDTH.value // 2, self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value // 2)
        down = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value)
        l = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2)

        self.coordinates.append(up)
        self.coordinates.append(r)
        self.coordinates.append(down)
        self.coordinates.append(l)


class CubeWallLeft:
    def __init__(self, centerUp):
        self.center = centerUp
        self.coordinates = []
        self.countCoords()
        self.color = WallColor.LEFT_WALL_COLOR.value

    def countCoords(self):
        up = (self.center[0] - BoardSize.TILE_WIDTH.value // 2, self.center[1])
        r = (self.center[0] - BoardSize.TILE_WIDTH.value // 2, self.center[1] + BoardSize.TILE_HEIGHT.value // 2 + BoardSize.CUBE_BREAK_HEIGHT.value // 2)
        down = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2 +  BoardSize.CUBE_BREAK_HEIGHT.value)
        l = (self.center[0], self.center[1] + BoardSize.TILE_HEIGHT.value // 2)

        self.coordinates.append(up)
        self.coordinates.append(l)
        self.coordinates.append(down)
        self.coordinates.append(r)
