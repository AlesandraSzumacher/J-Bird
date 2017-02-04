from jBird.utils.Constants import BoardSize, TileColor
from jBird.utils.LevelsUtils import TilesState


class TileControl:

    def changeColor(self, tile, boardDisplay):
        """Checking if the button is pressed."""
        for tileRomb in boardDisplay.tileRhombusList:
            if tileRomb.tile.center == tile.center:
                tileRomb.changeColor(TileColor.TOUCH_COLOR.value)
                if tile.state == TilesState.NOT_TOUCHED.value:
                    tile.change_state()



