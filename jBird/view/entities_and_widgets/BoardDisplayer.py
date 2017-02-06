from jBird.view.entities_and_widgets.TilePolygon import TilePolygon


class BoardDisplay:
    """Class for display board on screen"""

    def __init__(self, board):
        """Init board, prepares list of tiles and cube's walls."""
        self.board = board
        self.tile_rhombus_list = [TilePolygon(tile) for tile in self.board.list_of_tiles]
        self.cube_walls_list = [TilePolygon(wall, wall.color) for wall in self.board.list_of_cube_walls]

    def display_board(self, screen):
        """Places all tiles and cube's walls on screen."""
        for wall in self.cube_walls_list:
            screen = wall.draw_rhombus(screen)
        for tile in self.tile_rhombus_list:
            screen = tile.draw_rhombus(screen)

        return screen
