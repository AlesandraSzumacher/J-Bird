from enum import Enum


class ScreenSize(Enum):
    """Enum containing sizes of f screen."""
    WIDTH = 1201
    HEIGHT = 700


class PlayerPos(Enum):
    """Enum containing starting position of player."""
    START_WIDTH = 100
    START_HEIGHT = 100


class BoardSize(Enum):
    TILE_WIDTH = 80
    TILE_HEIGHT = 50
    CUBE_BREAK_HEIGHT = 50
    LEVELS_NUMBER = 7


class TileColor(Enum):
    START_COLOR = (0, 0, 255)
    TOUCH_COLOR = (0, 0, 0)
