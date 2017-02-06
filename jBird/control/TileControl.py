class TileControl:
    """Controling the operations on tiles."""

    def change_color(self, tile, board_display):
        """Changing the color of the tile."""
        for tile_romb in board_display.tile_rhombus_list:
            if tile_romb.tile.center == tile.center:
                tile_romb.change_color(tile.state.value)
