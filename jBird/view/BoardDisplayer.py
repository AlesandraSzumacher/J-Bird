from jBird.view.Rhombus import Rhombus


class BoardDisplay:
    def __init__(self, board):
        self.board = board
        self.tileRhombusList = [Rhombus(tile) for tile in self.board.listOfTiles]

    def displayBoard(self, screen):
        for tile in self.tileRhombusList:
            tile.draw_rhombus(screen)
        return screen