from jBird.utils.ScreenSize import BoardSize, TileColor


class TileControl:
    def changeColor(self, tile, boardDisplay):
        """Checking if the button is pressed."""
        for tileRomb in boardDisplay.tileRhombusList:
            if tileRomb.tile.center == tile.center:
                tileRomb.changeColor(TileColor.TOUCH_COLOR.value)

