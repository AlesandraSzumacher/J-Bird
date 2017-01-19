from pygame.constants import K_KP1
from pygame.constants import K_KP2
from pygame.constants import K_KP4
from pygame.constants import K_KP5

from jBird.utils.ScreenSize import BoardSize


class ChickenControl():
    def moveChicken(self, chicken, keyPressed, board):
        if chicken.level == -1:
            if keyPressed == K_KP1 or keyPressed == K_KP2:
                # kurczak rusza sie na pierwsza plytke w dol
                chicken.setTileCenter(board.listOfTiles[0].center)
                chicken.level = 0
            else:
                return chicken
        chicken = self.moveChickenDown(chicken, keyPressed, board)
        chicken = self.moveChickenUp(chicken, keyPressed, board)



        return chicken

    def moveChickenDown(self, chicken, keyPressed, board):
        possible_move_down = board.countTwoDownTiles(chicken.tile_center)
        choose_move = [0, 0]
        if keyPressed == K_KP1:
            choose_move = possible_move_down[0]
        elif keyPressed == K_KP2:
            choose_move = possible_move_down[1]

        if board.if_tile_is_in_board(choose_move):
            chicken.setTileCenter(choose_move)
            chicken.level += 1

        return chicken

    def moveChickenUp(self, chicken, keyPressed, board):
        possible_move_down = board.countNextUpTiles(chicken.tile_center)
        choose_move = [0, 0]
        if keyPressed == K_KP4:
            choose_move = possible_move_down[0]
        elif keyPressed == K_KP5:
            choose_move = possible_move_down[1]

        if board.if_tile_is_in_board(choose_move):
            chicken.setTileCenter(choose_move)
            chicken.level -= 1

        return chicken