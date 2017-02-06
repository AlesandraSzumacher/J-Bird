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
from jBird.logic.Game import Game
from jBird.utils.Constants import ScreenSize, Positions
from jBird.view.entities_and_widgets.BoardDisplayer import BoardDisplay
from jBird.view.entities_and_widgets.SnakeImage import SnakeImage

pygame.init()


class GameState:
    """Class containing methods and attributes referring to game state."""

    def __init__(self):
        """Initialization of GameState."""
        # Level1State()
        game = Game()
        folder = os.path.dirname(os.path.realpath(__file__))

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        font = pygame.font.SysFont("monospace", 40, True)
        level_label = font.render("Level: " + str(game.level), 1, (255, 255, 255))
        points_label = font.render("Points: " + str(game.board.number_of_touched_tiles), 1, (255, 255, 255))
        hp_label = font.render("Hp: " + str(game.player.hp), 1, (255, 255, 255))

        screen.blit(level_label, (0, 0))
        screen.blit(points_label, (0, 50))
        screen.blit(hp_label, (0, 100))

        board_dis = BoardDisplay(game.board)
        board_dis.display_board(screen)

        chicken_image = pygame.image.load(os.path.join(folder, "chickenFront.png"))
        ball_image = pygame.image.load(os.path.join(folder, "ball.png"))
        snake_image = SnakeImage()

        screen.blit(chicken_image, game.chicken.position)
        pygame.display.flip()

        FALL_DOWN_BALL = USEREVENT + 1
        pygame.time.set_timer(FALL_DOWN_BALL, 1500)

        MOVE_SNAKE = USEREVENT + 2
        pygame.time.set_timer(MOVE_SNAKE, 1500)

        clock = Clock()
        running = True
        not_frozen = True
        while running:

            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit(0)
                elif e.type == KEYDOWN and not_frozen:
                    controler = ChickenControl()

                    possible_move = controler.move_chicken(game.chicken, e.key, game.board)
                    if possible_move is None:
                        continue

                    tile = game.handle_level(possible_move)
                    if_collision = False

                    if tile == "NO_MORE_HP":
                        self.handle_lose(font, game, screen)
                        not_frozen = False
                        continue

                    if tile == "ONE_HP_LOST":
                        game.move_chicken_to_start_position()
                    else:
                        if_collision = game.check_collision_with_villains()
                        if not if_collision:
                            game.handle_touch_tile(tile)
                            tileControl = TileControl()
                            tileControl.change_color(tile, board_dis)

                    self.display_screen(font, background_colour, ball_image, board_dis, chicken_image, game,
                                        level_label, snake_image, screen)

                    if_lose = False
                    if if_collision:
                        if_lose = game.handle_collision_with_villain()
                        pygame.time.wait(500)

                    if if_lose:
                        self.handle_lose(font, game, screen)
                        not_frozen = False
                        continue

                    self.display_screen(font, background_colour, ball_image, board_dis, chicken_image, game,
                                        level_label, snake_image, screen)

                    if game.if_win():
                        if game.level == 3:
                            lose_label = font.render("Game End. You win! :)  ", 1, (255, 255, 255))
                            final_points = font.render("You score:   " + str(game.board.number_of_touched_tiles), 1,
                                                       (255, 255, 255))
                            screen.blit(lose_label, (350.5, 0))
                            screen.blit(final_points, (400.5, 50))
                            pygame.display.flip()
                            sys.exit(0)
                        else:
                            game.next_level()
                            game.board_for_next_level()
                            board_dis = BoardDisplay(game.board)

                            continue

                elif e.type == FALL_DOWN_BALL and not_frozen:
                    if len(game.list_of_villains) != 0:
                        for villain in game.list_of_villains:
                            if_ball_need_to_fall_down = villain.move_down(game.board)

                            if if_ball_need_to_fall_down:
                                game.list_of_villains.remove(villain)

                        self.display_screen(font, background_colour, ball_image, board_dis, chicken_image, game,
                                            level_label, snake_image, screen)

                        if_collision = game.check_collision_with_villains()
                        if if_collision:
                            if_lose = game.handle_collision_with_villain()
                            if if_lose:
                                self.handle_lose(font, game, screen)

                    if len(game.list_of_villains) < game.max_number_of_villains:
                        # losujemy i sprawdzimy czy nie powinno się cos pojawic
                        if_create_new_villain = random.randint(0, 10) % 2
                        if if_create_new_villain == 1:
                            game.add_villain()

                        self.display_screen(font, background_colour, ball_image, board_dis, chicken_image, game,
                                            level_label, snake_image, screen)
                        continue

                elif e.type == MOVE_SNAKE and not_frozen:
                    if game.snake is None:
                        if_create_new_villain = random.randint(0, 100) % 3
                        if if_create_new_villain == 1:
                            game.add_snake()
                            snake_image = SnakeImage()
                        else:
                            continue
                    else:
                        game.move_snake()
                        if not game.snake.if_ball:
                            snake_image.change_ball_into_snake()

                        self.display_screen(font, background_colour, ball_image, board_dis, chicken_image, game,
                                            level_label, snake_image, screen)

                        if_collision = game.check_collision_with_villains()
                        if if_collision:
                            if_lose = game.handle_collision_with_villain()
                            if if_lose:
                                self.handle_lose(font, game, screen)
                                not_frozen = False

    def handle_lose(self, font, game, screen):
        lose_label = font.render("Game End. You lost :(  ", 1, (255, 255, 255))
        final_points = font.render("You score:   " + str(game.board.number_of_touched_tiles), 1,
                                   (255, 255, 255))
        screen.blit(lose_label, (350.5, 0))
        screen.blit(final_points, (400.5, 50))
        pygame.display.flip()

    def display_screen(self, arialFont, background_colour, ball_image, boardDis, chicken_image, game, level_label,
                       snake_image, screen):
        """Display widgets on screen"""
        screen.fill(background_colour)
        boardDis.display_board(screen)
        level_label = arialFont.render("Level: " + str(game.level), 1, (255, 255, 255))
        screen.blit(level_label, (0, 0))
        points_label = arialFont.render("Points: " + str(game.save_porints + game.board.number_of_touched_tiles), 1, (255, 255, 255))
        screen.blit(points_label, (0, 50))
        hp_label = arialFont.render("Hp: " + str(game.player.hp), 1, (255, 255, 255))
        screen.blit(hp_label, (0, 100))
        screen.blit(chicken_image, game.chicken.get_position())

        if game.snake is not None:
            screen.blit(snake_image.image, game.snake.get_position())

        for villain in game.list_of_villains:
            screen.blit(ball_image, villain.get_position())
        pygame.display.flip()
