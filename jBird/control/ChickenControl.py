import sys
from pygame.constants import K_1
from pygame.constants import K_EQUALS
from pygame.constants import K_KP1
from pygame.constants import K_KP2
from pygame.constants import K_KP3
from pygame.constants import K_KP4
from pygame.constants import K_KP5
from pygame.constants import K_KP7
from pygame.constants import K_KP9
from pygame.constants import K_p
from pygame.constants import K_w


class ChickenControl():
    """Containing methods to move the chicken on the board."""

    def moveChicken(self, chicken, keyPressed, board):
        """Allows to move the chicken - uses methods moveChickenDown and moveChickenUp."""
        if chicken.level == -1:
            return board.listOfTiles[0].center

        possible_move1 = self.moveChickenDown(chicken, keyPressed, board)
        possible_move2 = self.moveChickenUp(chicken, keyPressed, board)

        if possible_move1 is None:
            return possible_move2
        return possible_move1

    def moveChickenDown(self, chicken, keyPressed, board):
        """Allows to move the chicken down - left or right."""
        possible_move_down = board.countTwoDownTiles(chicken.tile_center)
        choose_move = None
        if keyPressed in [K_KP1, K_w]:
            choose_move = possible_move_down[0]
        elif keyPressed in [K_KP3, K_p]:
            choose_move = possible_move_down[1]

        return choose_move
        # if board.if_tile_is_in_board(choose_move):
        #     chicken.setTileCenter(choose_move)
        #     chicken.level += 1
        # elif keyPressed in [K_KP1, K_w, K_KP3, K_p]:
        #     return sys.exit(0)

    def moveChickenUp(self, chicken, keyPressed, board):
        """Allows to move the chicken up - left or right."""
        possible_move_down = board.countNextUpTiles(chicken.tile_center)
        choose_move = None
        if keyPressed in [K_KP7, K_1]:
            choose_move = possible_move_down[0]
        elif keyPressed in [K_KP9, K_EQUALS]:
            choose_move = possible_move_down[1]

        return choose_move
        # if board.if_tile_is_in_board(choose_move):
        #     chicken.setTileCenter(choose_move)
        #     # chicken.level -= 1
        # elif keyPressed in [K_KP7, K_1, K_KP9, K_EQUALS]:
        #     return sys.exit(0)
