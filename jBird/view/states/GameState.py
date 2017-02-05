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
        pygame.display.flip()

        FALL_DOWN_BALL = USEREVENT + 1
        pygame.time.set_timer(FALL_DOWN_BALL, 1500)

        number_of_created_villain = 0

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

                    tile = game.handle_level(possible_move)
                    if_collision = False

                    if tile == "NO_MORE_HP":
                        #TODO
                        sys.exit(0)

                    if tile == "ONE_HP_LOST":
                        game.move_chicken_to_start_position()
                    else:
                        if_collision = game.check_collision_with_villains()
                        if not if_collision:
                            game.handle_touch_tile(tile)
                            tileControl = TileControl()
                            tileControl.changeColor(tile, boardDis)

                    self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                        level_label, player_label, screen)

                    if_loose = False
                    if if_collision:
                        is_villan = 0
                        if_loose = game.handle_collision_with_villain()
                        pygame.time.wait(500)

                    self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                        level_label, player_label, screen)

                    if if_loose:
                        # TODO
                        sys.exit(0)

                    if game.if_win():
                        # TODO
                        print("win win win")
                        if game.level == 3:
                            sys.exit(0)
                        else:
                            game.next_level()
                            game.board_for_next_level()
                            boardDis = BoardDisplay(game.board)

                            continue

                elif e.type == FALL_DOWN_BALL:
                    print("numer ", number_of_created_villain)
                    if number_of_created_villain != 0:
                        for villain in game.list_of_villains:
                            if_ball_need_to_fall_down = villain.move_down(game.board)

                            if if_ball_need_to_fall_down:
                                game.list_of_villains.remove(villain)
                                number_of_created_villain -= 1

                        self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                            level_label, player_label, screen)

                        if_collision = game.check_collision_with_villains()
                        print("czy byla kolizja ", if_collision)
                        if if_collision:
                            print("Kolizja")
                            number_of_created_villain = 0
                            if_loose = game.handle_collision_with_villain()
                            # pygame.time.wait(500)

                    if number_of_created_villain < 2:
                        print("losujemy")
                        # losujemy i sprawdzimy czy nie powinno się cos pojawic
                        if_create_new_villain = random.randint(0, 10) % 2
                        print(if_create_new_villain)
                        if if_create_new_villain == 1:
                            number_of_created_villain += 1
                            game.add_villain()

                        self.display_screen(arialFont, background_colour, ball_image, boardDis, chicken_image, game,
                                                level_label, player_label, screen)
                        continue




    def display_screen(self, arialFont, background_colour, ball_image, boardDis, chicken_image, game, level_label,
                       player_label, screen):
        """Display widgets on screen"""
        screen.fill(background_colour)
        boardDis.displayBoard(screen)
        screen.blit(player_label, (0, 0))
        screen.blit(level_label, (0, 50))
        points_label = arialFont.render("Points: " + str(game.board.numberOfTouchedTiles), 1, (95, 27, 84))
        screen.blit(points_label, (0, 100))
        hp_label = arialFont.render("Hp: " + str(game.player.hp), 1, (95, 27, 84))
        screen.blit(hp_label, (0, 150))
        screen.blit(chicken_image, game.chicken.getPosition())
        for villain in game.list_of_villains:
            screen.blit(ball_image, villain.get_position())
        pygame.display.flip()
