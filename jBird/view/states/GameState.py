import os
import sys

import pygame
import pygame.constants
from pygame.constants import KEYDOWN
from pygame.constants import QUIT
from pygame.time import Clock

from jBird.control.ChickenControl import ChickenControl
from jBird.control.TileControl import TileControl
from jBird.logic.Chicken import Chicken
from jBird.logic.Game import Game
from jBird.utils.Constants import ScreenSize, Positions
from jBird.view.entities_and_widgets.BoardDisplayer import BoardDisplay

pygame.init()


class GameState:
    def __init__(self):
        game = Game()
        folder = os.path.dirname(os.path.realpath(__file__))

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        arialFont = pygame.font.SysFont("arial", 40)
        player_label = arialFont.render("Player: " + str(game.player.nick), 1, (95, 27, 84))
        level_label = arialFont.render("Level: " + str(game.level), 1, (95, 27, 84))
        points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))
        hp_label = arialFont.render("Hp: " + str(game.player.hp), 1, (95, 27, 84))

        screen.blit(player_label, (0, 0))
        screen.blit(level_label, (0, 50))
        screen.blit(points_label, (0, 100))
        screen.blit(hp_label, (0, 150))

        boardDis = BoardDisplay(game.board)
        boardDis.displayBoard(screen)

        chicken_image = pygame.image.load(os.path.join(folder, "chickenFront.png"))
        ball_image = pygame.image.load(os.path.join(folder, "ball.png"))

        screen.blit(chicken_image, game.chicken.position)
        game.add_villain()
        screen.blit(ball_image, game.list_of_villains[0].get_position())

        pygame.display.flip()

        clock = Clock()
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

                    tile, if_win = game.handle_level(possible_move)

                    if tile == "NO_MORE_HP":
                        sys.exit(0)

                    if tile == "ONE_HP_LOST":
                        game.move_chicken_to_start_position()
                    else:

                        tileControl = TileControl()
                        tileControl.changeColor(tile, boardDis)

                    screen.fill(background_colour)
                    boardDis.displayBoard(screen)
                    screen.blit(player_label, (0, 0))
                    screen.blit(level_label, (0, 50))

                    points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))
                    screen.blit(points_label, (0, 100))

                    hp_label = arialFont.render("Hp: " + str(game.player.hp), 1, (95, 27, 84))
                    screen.blit(hp_label, (0, 150))
                    screen.blit(chicken_image, game.chicken.getPosition())
                    pygame.display.flip()

                    if if_win:
                        sys.exit(0)
