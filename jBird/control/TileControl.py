from jBird.utils.ScreenSize import BoardSize, TileColor


class TileControl:
    def pressed(self, center, mouse):
        """Check only rectangle in rhombus"""
        if (center[0] - BoardSize.TILE_WIDTH.value//4) <= mouse[0] <= (center[0] + BoardSize.TILE_WIDTH.value//4) \
                and (center[1] - BoardSize.TILE_HEIGHT.value//4) <= mouse[1] <= (center[1] + BoardSize.TILE_HEIGHT.value//4):
            print("Now I have to change color!")
            return True
        else:
            return False

    def changeColor(self, tile, boardDisplay):
        for tileRomb in boardDisplay.tileRhombusList:
            if tileRomb.tile.center == tile.center:
                tileRomb.changeColor(TileColor.TOUCH_COLOR.value)

