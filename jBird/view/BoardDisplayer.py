from jBird.view.TilePolygon import TilePolygon


class BoardDisplay:
    def __init__(self, board):
        self.board = board
        self.tileRhombusList = [TilePolygon(tile) for tile in self.board.listOfTiles]
        self.cubeWallsList = [TilePolygon(wall, wall.color) for wall in self.board.listOfCubeWalls]

    def displayBoard(self, screen):
        for wall in self.cubeWallsList:
            screen = wall.draw_rhombus(screen)
        for tile in self.tileRhombusList:
            screen = tile.draw_rhombus(screen)

        return screen
