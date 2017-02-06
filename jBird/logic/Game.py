import pygame

from jBird.logic.Board import Board
from jBird.logic.Chicken import Chicken
from jBird.logic.Player import Player
from jBird.logic.Snake import Snake
from jBird.logic.Villain import Villain
from jBird.utils.Constants import ScreenSize, Positions, BoardSize
from jBird.utils.LevelsUtils import NumberOfTiles
from jBird.utils.LevelsUtils import MaxNumberOfVillains
from jBird.view.states.LevelsState import Level1State, Level2State, Level3State


class Game(object):
    """Class containing  methods which refer to game, such as levels and rounds."""

    def __init__(self):
        """Initializing new Game."""
        Level1State()
        self.snake = None
        self.level = 1
        self.round = 1
        self.save_porints = 0
        self.board = Board([ScreenSize.WIDTH.value // 2, Positions.BOARD_DOWN.value], BoardSize.LEVELS_NUMBER.value)
        self.player = Player("Ola")
        self.chicken = Chicken()
        self.max_number_of_villains = MaxNumberOfVillains.LEVEL_1.value

        self.list_of_villains = []

    def next_level(self):
        """Changing level into next."""
        self.level += 1
        self.save_porints = self.board.number_of_touched_tiles
        self.max_number_of_villains = MaxNumberOfVillains.LEVEL_2_3.value
        pygame.time.wait(1000)

        if self.level == 2:
            Level2State()
        else:
            Level3State()

    def next_round(self):
        """Changing round into next or into first in the new level."""
        self.round = ((self.round + 1) % 3) + 1

    def check_collision_with_villains(self):
        """Checks if chicken collides with any of the villains."""
        v = self.snake
        if v is not None and v.position[0] == self.chicken.tile_center[0] and v.position[1] == self.chicken.tile_center[
            1]:
            return True
        for v in self.list_of_villains:
            if v.position[0] == self.chicken.tile_center[0] and v.position[1] == self.chicken.tile_center[1]:
                return True
        return False

    def handle_level(self, move):
        """Handling single level."""
        if_correct_move = self.board.if_tile_is_in_board(move)

        if if_correct_move is False:
            self.player.sub_hp()
            if self.player.hp < 0:
                return "NO_MORE_HP"
            return "ONE_HP_LOST"

        self.chicken.set_tile_center(move)

        tile = self.board.return_tile_from_board(move)

        return tile

    def if_win(self):
        """Checks if the player finished the level successfully."""
        if self.level == 1:
            if self.board.number_of_touched_tiles == NumberOfTiles.LEVEL_1.value:
                return True
        else:
            if self.board.number_of_touched_tiles == NumberOfTiles.LEVEL_1.value * 2:
                return True
        return False

    def move_chicken_to_start_position(self):
        """Move chicken to start position, usualy after collision or fall down"""
        self.chicken.move_to_start_position()

    def add_villain(self):
        """Create a new villain on list of villains"""
        self.list_of_villains.append(Villain(self.board))
        return self.list_of_villains[len(self.list_of_villains) - 1]

    def handle_collision_with_villain(self):
        """Move chicken to start position, substract hp and villain disappear"""
        self.move_chicken_to_start_position()
        self.player.sub_hp()
        self.list_of_villains = []
        self.snake = None
        return self.player.hp < 0

    def handle_touch_tile(self, tile):
        """Handling touching the tile by chicken."""
        change_status = tile.change_state(self.level)
        if change_status == 1:
            self.board.increase_number_of_touched_tiles()
        elif change_status == -1:
            self.board.decrease_number_of_touched_tiles()

    def board_for_next_level(self):
        """Remove all villains, make new board and new chicken."""
        self.list_of_villains = []
        self.snake = None
        self.board = Board([ScreenSize.WIDTH.value // 2, Positions.BOARD_DOWN.value], BoardSize.LEVELS_NUMBER.value)
        self.chicken = Chicken()

    def add_snake(self):
        """Adds snake in ball."""
        self.snake = Snake(self.board)
        return self.snake

    def move_snake(self):
        """Moves snake."""
        self.snake.move(self.board, self.chicken)
