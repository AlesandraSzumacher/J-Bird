from pygame.constants import K_1
from pygame.constants import K_EQUALS
from pygame.constants import K_KP1
from pygame.constants import K_KP3

from pygame.constants import K_KP7
from pygame.constants import K_KP9
from pygame.constants import K_p
from pygame.constants import K_w


class ChickenControl:
    """Containing methods to move the chicken on the board."""

    def move_chicken(self, chicken, key_pressed, board):
        """Allows to move the chicken - uses methods moveChickenDown and moveChickenUp."""
        if chicken.level == -1:
            return board.list_of_tiles[0].center

        possible_move1 = self.move_chicken_down(chicken, key_pressed, board)
        possible_move2 = self.move_chicken_up(chicken, key_pressed, board)

        if possible_move1 is None:
            return possible_move2
        return possible_move1

    def move_chicken_down(self, chicken, key_pressed, board):
        """Allows to move the chicken down - left or right."""
        possible_move_down = board.count_two_down_tiles(chicken.tile_center)
        choose_move = None
        if key_pressed in [K_KP1, K_w]:
            choose_move = possible_move_down[0]
        elif key_pressed in [K_KP3, K_p]:
            choose_move = possible_move_down[1]
        return choose_move

    def move_chicken_up(self, chicken, key_pressed, board):
        """Allows to move the chicken up - left or right."""
        possible_move_up = board.count_next_up_tiles(chicken.tile_center)
        choose_move = None
        if key_pressed in [K_KP7, K_1]:
            choose_move = possible_move_up[0]
        elif key_pressed in [K_KP9, K_EQUALS]:
            choose_move = possible_move_up[1]

        return choose_move
