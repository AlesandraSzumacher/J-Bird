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
        player_label = arialFont.render("Player: " + str(game.player.nick), 1, (95, 27, 84))
        level_label = arialFont.render("Level: " + str(game.level), 1, (95, 27, 84))
        points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))

        screen.blit(player_label, (0, 0))
        screen.blit(level_label, (0, 50))
        screen.blit(points_label, (0, 100))


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

                    possible_move = controler.moveChicken(game.chicken, e.key, game.board)
                    if possible_move is None:
                        continue

                    tile = game.handle_level(possible_move)

                    tileControl = TileControl()
                    tileControl.changeColor(tile, boardDis)

                    # tile = game.board.return_tile_from_board(game.chicken.tile_center)
                    # tileControl = TileControl()
                    # tileControl.changeColor(tile, boardDis)

                    screen.fill(background_colour)
                    boardDis.displayBoard(screen)
                    screen.blit(player_label, (0, 0))
                    screen.blit(level_label, (0, 50))

                    points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))
                    screen.blit(points_label, (0, 100))

                    screen.blit(chicken_image, chicken.getPosition())
                    pygame.display.flip()
