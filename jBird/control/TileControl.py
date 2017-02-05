class TileControl:
    """Controling the operations on tiles."""

    def changeColor(self, tile, boardDisplay):
        """Changing the color of the tile."""
        for tileRomb in boardDisplay.tileRhombusList:
            if tileRomb.tile.center == tile.center:
                tileRomb.changeColor(tile.state.value)
