from enum import Enum


class NumberOfTiles(Enum):
    """Enum containing number of tiles for all levels."""
    LEVEL_1 = 28


class NumberOfNeededTouches(Enum):
    """Enum containing number of needed touches for specific level."""
    Level_1 = 1


class TilesState(Enum):
    """Enum containing states of tiles."""
    NOT_TOUCHED = 0
    TOUCHED = 1
