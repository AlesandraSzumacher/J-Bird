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
    """Enum containing size of the Board."""
    TILE_WIDTH = 80
    TILE_HEIGHT = 50
    CUBE_BREAK_HEIGHT = 50
    LEVELS_NUMBER = 7


class TileColor(Enum):
    """Enum containing color of the Tile in RGB."""
    START_COLOR = (255, 255, 168)
    TOUCH_COLOR = (185, 7, 7)
    DOUBLE_TOUCH_COLOR = (255, 120, 120)


class WallColor(Enum):
    """Enum containing color of the Wall in RGB."""
    LEFT_WALL_COLOR = (0, 0, 30)
    RIGHT_WALL_COLOR = (166, 41, 79)


class Positions(Enum):
    """Enum containing starting position of chicken."""
    CHICKEN_INIT_POSITION = (ScreenSize.WIDTH.value / 2 - 30, 10)
    BOARD_DOWN = 150



