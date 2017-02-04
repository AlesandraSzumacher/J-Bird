import pygame
import sys

from jBird.control.TileControl import TileControl
from jBird.logic.Board import Board
from jBird.logic.Chicken import Chicken
from jBird.logic.Player import Player
from jBird.logic.Villain import Villain
from jBird.utils.Constants import ScreenSize, Positions
from jBird.utils.LevelsUtils import NumberOfTiles




class Game(object):
    """Class containing  methods which refer to game, such as levels and rounds."""
    def __init__(self):
        """Initializing new Game."""
        self.level = 1
        self.round = 1
        self.board = Board([ScreenSize.WIDTH.value//2, Positions.BOARD_DOWN.value])
        self.player = Player("Ola")
        self.chicken = Chicken()

        self.list_of_villains = []

    def next_level(self):
        """Changing level into next."""
        self.level += 1

    def next_round(self):
        """Changing round into next or into first in the new level."""
        self.round = ((self.round + 1) % 3) + 1

    def handle_level(self, move):
        if_correct_move = self.board.if_tile_is_in_board(move)
        if if_correct_move is False:
            self.player.hp -= 1
            if self.player.hp < 0:
                return ["NO_MORE_HP", False]
            # sys.exit(0)
            return ["ONE_HP_LOST", False]

        self.chicken.setTileCenter(move)
        tile = self.board.return_tile_from_board(move)

        if tile.change_state():
            self.board.increaseNumberOfTouchedTiles()

        if self.board.numberOfTouchedTiles == NumberOfTiles.LEVEL_1.value:
            return [tile, True]

        return [tile, False]

    def move_chicken_to_start_position(self):
        self.chicken.move_to_start_position()

    def add_villain(self):
        self.list_of_villains.append(Villain(self.board))
        return self.list_of_villains[0]
