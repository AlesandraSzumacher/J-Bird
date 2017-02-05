from enum import Enum
from jBird.utils.Constants import TileColor


class NumberOfTiles(Enum):
    """Enum containing number of tiles for all levels."""
    LEVEL_1 = 28


class NumberOfNeededTouches(Enum):
    """Enum containing number of needed touches for specific level."""
    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 2


class TilesState(Enum):
    """Enum containing states of tiles."""
    NOT_TOUCHED = TileColor.START_COLOR.value
    TOUCHED = TileColor.TOUCH_COLOR.value
    DOUBLE_TOUCHED = TileColor.DOUBLE_TOUCH_COLOR.value


class MaxNumberOfVillains(Enum):
    """Contains number of villians on the board for specific level."""
    LEVEL_1 = 2
    LEVEL_2_3 = 3
