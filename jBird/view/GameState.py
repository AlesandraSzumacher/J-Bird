import pygame
import pygame.constants
import sys
from pygame.constants import KEYDOWN
from pygame.constants import K_DOWN
from pygame.constants import K_KP0
from pygame.constants import K_KP1
from pygame.constants import K_KP2
from pygame.constants import K_KP4
from pygame.constants import K_KP5

from pygame.constants import MOUSEBUTTONDOWN
from pygame.constants import QUIT

from jBird.logic.Chicken import Chicken
from jBird.logic.Game import Game
from jBird.utils.ScreenSize import ScreenSize, TileColor, PlayerPos, Positions, BoardSize
from jBird.view.BoardDisplayer import BoardDisplay

pygame.init()


class Position(object):
    pass


class GameState:
    def __init__(self):
        game = Game()

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))
        playerPosition = (PlayerPos.START_HEIGHT.value, PlayerPos.START_WIDTH.value)
        keys = [False, False, False, False]

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        arialFont = pygame.font.SysFont("arial", 40)
        player_label = arialFont.render("Player: ", 1, (0, 255, 0))
        screen.blit(player_label, (0, 0))

        boardDis = BoardDisplay(game.board)
        boardDis.displayBoard(screen)

        chicken = Chicken()
        chicken_image = pygame.image.load("kurczaczunio.png")


        screen.blit(chicken_image, chicken.position)

        pygame.display.flip()



        running = True

        while running:
            for e in pygame.event.get():
                currentTile = 0
                if e.type == QUIT:
                    sys.exit(0)
                elif e.type == KEYDOWN:
                    if e.key == K_KP1 and chicken.level == -1:
                        chicken.level = 0
                        currentTile = game.board.listOfTiles[0]
                        chicken.move_down_tile(currentTile)

                    elif chicken.level == 0:
                        current_tile_center = chicken.tile_center
                        left_next_tiles = game.board.countTwoDownTiles(current_tile_center)[0]
                        right_next_tiles = game.board.countTwoDownTiles(current_tile_center)[1]

                        if e.key == K_KP1:
                            chicken.level = 1
                            chicken.move_down(left_next_tiles)
                        elif K_KP2 == e.key:
                            chicken.level = 1
                            chicken.move_down(right_next_tiles)

                    elif chicken.level != BoardSize.LEVELS_NUMBER.value - 1:
                        current_tile_center = chicken.tile_center
                        next_tiles_down = game.board.countTwoDownTiles(current_tile_center)
                        next_tiles_up = game.board.countNextUpTiles(current_tile_center)

                        if e.key == K_KP1:
                            chicken.level += 1
                            chicken.move_down(next_tiles_down[0])
                        elif K_KP2 == e.key:
                            chicken.level += 1
                            chicken.move_down(next_tiles_down[1])
                        elif e.key == K_KP4:
                            chicken.level -= 1
                            chicken.move_down(next_tiles_up[0])
                        elif K_KP5 == e.key:
                            chicken.level -= 1
                            chicken.move_down(next_tiles_up[1])

                    elif chicken.level == BoardSize.LEVELS_NUMBER.value - 1:
                        current_tile_center = chicken.tile_center
                        next_tiles_up = game.board.countNextUpTiles(current_tile_center)
                        if e.key == K_KP4:
                            chicken.level -= 1
                            chicken.move_down(next_tiles_up[0])
                        elif K_KP5 == e.key:
                            chicken.level -= 1
                            chicken.move_down(next_tiles_up[1])

                    if game.board.if_tile_is_in_board(chicken.tile_center):
                        screen.fill(background_colour)
                        boardDis.displayBoard(screen)
                        screen.blit(player_label, (0, 0))
                        screen.blit(chicken_image, chicken.position)
                        pygame.display.flip()


5
                        #boardDis.displayBoard(screen)
                #pygame.display.flip()
                #   print("done")

# GameState()
