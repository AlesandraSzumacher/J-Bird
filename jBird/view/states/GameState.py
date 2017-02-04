import sys

import pygame
import pygame.constants
from pygame.constants import KEYDOWN
from pygame.constants import QUIT

from jBird.control.ChickenControl import ChickenControl
from jBird.control.TileControl import TileControl
from jBird.logic.Chicken import Chicken
from jBird.logic.Game import Game
from jBird.utils.Constants import ScreenSize
from jBird.view.entities_and_widgets.BoardDisplayer import BoardDisplay

pygame.init()


class GameState:
    def __init__(self):
        game = Game()

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        arialFont = pygame.font.SysFont("arial", 40)
        player_label = arialFont.render("Player: ", 1, (95, 27, 84))
        screen.blit(player_label, (0, 0))

        boardDis = BoardDisplay(game.board)
        boardDis.displayBoard(screen)

        chicken = Chicken()
        chicken_image = pygame.image.load("chickenFront.png")

        screen.blit(chicken_image, chicken.position)

        pygame.display.flip()

        running = True

        while running:
            for e in pygame.event.get():

                if e.type == QUIT:
                    sys.exit(0)
                elif e.type == KEYDOWN:
                    controler = ChickenControl()
                    controler.moveChicken(chicken, e.key, game.board)

                    tile = game.board.return_tile_from_board(chicken.tile_center)
                    tileControl = TileControl()
                    tileControl.changeColor(tile, boardDis)

                    screen.fill(background_colour)
                    boardDis.displayBoard(screen)
                    screen.blit(player_label, (0, 0))

                    screen.blit(chicken_image, chicken.getPosition())
                    pygame.display.flip()