import pygame
import pygame.constants
import sys
from pygame.constants import KEYDOWN
from pygame.constants import K_DOWN

from pygame.constants import MOUSEBUTTONDOWN
from pygame.constants import QUIT

from jBird.logic.Chicken import Chicken
from jBird.logic.Game import Game
from jBird.utils.ScreenSize import ScreenSize, TileColor, PlayerPos, Positions
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
        chicken_image = pygame.image.load("kurczak.jpg")


        screen.blit(chicken_image, chicken.position)

        pygame.display.flip()



        running = True

        while running:
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
                elif e.type == KEYDOWN:
                    if e.key == K_DOWN and chicken.direction == "INIT DOWN":
                        print("w doł")

                        # przyciag do środka pierwszej płytki
                        direction = "DOWN"
                        chicken.move(direction)
                        screen.blit(chicken_image, chicken.position)
                        pygame.display.flip()

                    print("cos")

                #boardDis.displayBoard(screen)
                #pygame.display.flip()
                #   print("done")


GameState()
