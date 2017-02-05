import os
import random
import sys

import pygame
import pygame.constants
from pygame.constants import KEYDOWN
from pygame.constants import QUIT
from pygame.constants import USEREVENT
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
        # screen.blit(ball_image, game.list_of_villains[0].get_position())

        pygame.display.flip()

        FALL_DOWN_BALL = USEREVENT + 1
        pygame.time.set_timer(FALL_DOWN_BALL, 1500)

        is_villan = False

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
                    if_collision = False

                    if tile == "NO_MORE_HP":
                        sys.exit(0)

                    if tile == "ONE_HP_LOST":
                        game.move_chicken_to_start_position()
                    else:
                        if_collision = game.check_collision_with_villains()
                        if not if_collision:
                            tileControl = TileControl()
                            tileControl.changeColor(tile, boardDis)

                    self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                        level_label, player_label, screen)

                    pygame.display.flip()

                    if if_win:
                        sys.exit(0)

                    if if_collision:
                        sys.exit(0)

                elif e.type == FALL_DOWN_BALL:
                    if not is_villan:
                        # losujemy i sprawdzimy czy nie powinno się cos pojawic
                        is_villan = random.randint(0, 10) % 2
                        if is_villan == 0:
                            is_villan = False
                        else:
                            is_villan = True
                            game.add_villain()

                            self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                                level_label, player_label, screen)

                            pygame.display.flip()
                            continue

                    if is_villan:
                        if_dont_remove = game.list_of_villains[0].move_down(game.board)
                        if not if_dont_remove:
                            game.list_of_villains.remove(game.list_of_villains[0])
                            is_villan = False
                            continue

                        self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                            level_label, player_label, screen)

                        pygame.display.flip()

    def display_screen(self, arialFont, background_colour, ball_image, boardDis, chicken_image, game, level_label,
                       player_label, screen):
        screen.fill(background_colour)
        boardDis.displayBoard(screen)
        screen.blit(player_label, (0, 0))
        screen.blit(level_label, (0, 50))
        points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))
        screen.blit(points_label, (0, 100))
        hp_label = arialFont.render("Hp: " + str(game.player.hp), 1, (95, 27, 84))
        screen.blit(hp_label, (0, 150))
        screen.blit(chicken_image, game.chicken.getPosition())
        if len(game.list_of_villains) > 0:
            screen.blit(ball_image, game.list_of_villains[0].get_position())
