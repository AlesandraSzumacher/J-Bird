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

    def check_collision_with_villains(self):
        """Checks if chicken collides with any of the villains."""
        for v in self.list_of_villains:
            if v.position[0] == self.chicken.tile_center[0] and  v.position[1] == self.chicken.tile_center[1]:
                return True
        return False

    def handle_level(self, move):
        """Handling sigle level."""
        if_correct_move = self.board.if_tile_is_in_board(move)

        if if_correct_move is False:
            self.player.sub_hp()
            if self.player.hp < 0:
                return "NO_MORE_HP"
            return "ONE_HP_LOST"

        self.chicken.setTileCenter(move)

        tile = self.board.return_tile_from_board(move)

        return tile

    def if_win(self):
        """Checks if the player finished the level successfully."""
        if self.level == 1:
            if self.board.numberOfTouchedTiles == NumberOfTiles.LEVEL_1.value:
                return True
        else:
            if self.board.numberOfTouchedTiles == NumberOfTiles.LEVEL_1.value * 2:
                return True
        return False

    def move_chicken_to_start_position(self):
        """Move chicken to start position, usualy after collision or fall down"""
        self.chicken.move_to_start_position()

    def add_villain(self):
        """Create a new villain on list of villains"""
        self.list_of_villains.append(Villain(self.board))
        return self.list_of_villains[len(self.list_of_villains)-1]

    def handle_collision_with_villain(self):
        """Move chicken to start position, substract hp and villain disappear"""
        self.move_chicken_to_start_position()
        self.player.sub_hp()
        self.list_of_villains.clear()
        return self.player.hp < 0

    def handle_touch_tile(self, tile):
        """Handling touching the tile by chicken."""
        change_status = tile.change_state(self.level)
        if change_status == 1:
            self.board.increaseNumberOfTouchedTiles()
        elif change_status == -1:
            self.board.decreaseNumberOfTouchedTiles()

    def board_for_next_level(self):
        self.board = Board([ScreenSize.WIDTH.value // 2, Positions.BOARD_DOWN.value])
        self.chicken = Chicken()
