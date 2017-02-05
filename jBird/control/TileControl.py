from jBird.utils.Constants import BoardSize, TileColor
from jBird.utils.LevelsUtils import TilesState


class TileControl:

    def changeColor(self, tile, boardDisplay):
        """Changing the color of the tile."""
        for tileRomb in boardDisplay.tileRhombusList:
            if tileRomb.tile.center == tile.center:
                tileRomb.changeColor(tile.state.value)
                # if tile.state == TilesState.NOT_TOUCHED.value:
                #     return tile.change_state(level)

        return 0





