import os

import pygame

from jBird.control.TileControl import TileControl
from jBird.logic.Board import Board
from jBird.logic.Chicken import Chicken
from jBird.utils.Constants import ScreenSize
from jBird.utils.LevelsUtils import TilesState
from jBird.view.entities_and_widgets.BoardDisplayer import BoardDisplay

pygame.init()


class LevelState:
    """Class derived by states."""

    def __init__(self):
        """Init state"""

        folder = os.path.dirname(os.path.realpath(__file__))

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('J-Bird')

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        arial_font = pygame.font.SysFont("monospace", 80, True)
        level_label = self.level_label(arial_font)

        board = Board([600.5, 350], 2)

        board_disp = BoardDisplay(board)

        self.animation(background_colour, board, board_disp, folder, level_label, screen)

        pygame.time.wait(1000)

    def make_animation_move(self, board, board_disp, chicken, moves_to_do, which_time=1):
        """Moves chicken in animation."""
        chicken.set_tile_center(moves_to_do)
        tile = board.return_tile_from_board(moves_to_do)
        if which_time == 1:
            self.change_color(board_disp, tile)
        elif which_time == 2:
            self.change_color_second_time(board_disp, tile)
        elif which_time == 3:
            self.change_color_to_first(board_disp, tile)

    def change_color(self, board_disp, tile):
        """Changes color of tiles in board."""
        tile.state = TilesState.TOUCHED
        tileControl = TileControl()
        tileControl.change_color(tile, board_disp)

    def change_color_second_time(self, board_disp, tile):
        """Changes color of tiles in board."""
        tile.state = TilesState.DOUBLE_TOUCHED
        tileControl = TileControl()
        tileControl.change_color(tile, board_disp)

    def display_on_screen(self, background_colour, board_disp, chicken, chicken_image, level_label, screen):
        """Display all widgets on board"""
        screen.fill(background_colour)

        rect1 = level_label.get_rect(center=(ScreenSize.WIDTH.value / 2, 100))

        screen.blit(level_label, rect1)
        board_disp.display_board(screen)
        screen.blit(chicken_image, chicken.get_position())
        pygame.display.flip()
        pygame.time.wait(500)

    def change_color_to_first(self, board_disp, tile):
        """Changes color of tiles in board."""
        tile.state = TilesState.NOT_TOUCHED
        tileControl = TileControl()
        tileControl.change_color(tile, board_disp)


class Level1State(LevelState):
    """Class making animation how to play in 1. level."""

    def level_label(self, arial_font):
        level_label = arial_font.render("LEVEL 1", 1,  (255, 255, 255))
        return level_label

    def animation(self, background_colour, board, board_disp, folder, level_label, screen):
        """Makes animation for 1 level."""
        chicken = Chicken()
        chicken.set_tile_center([600.5, 350])
        chicken_image = pygame.image.load(os.path.join(folder, "chickenFront.png"))
        self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)
        moves_to_do = board.count_two_down_tiles([600.5, 350])
        moves = [moves_to_do[0], [600.5, 350], moves_to_do[1], [600.5, 350]]

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)


class Level2State(LevelState):
    """Class making animation how to play in 2. level."""

    def level_label(self, arial_font):
        level_label = arial_font.render("LEVEL 2", 1,  (255, 255, 255))
        return level_label

    def animation(self, background_colour, board, board_disp, folder, level_label, screen):
        """Makes animation for 2 level."""
        chicken = Chicken()
        chicken.set_tile_center([600.5, 350])
        chicken_image = pygame.image.load(os.path.join(folder, "chickenFront.png"))
        self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)
        moves_to_do = board.count_two_down_tiles([600.5, 350])
        moves = [moves_to_do[0], [600.5, 350], moves_to_do[1], [600.5, 350]]

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move, 2)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)


class Level3State(LevelState):
    """Class making animation how to play in 3. level."""

    def level_label(self, arial_font):
        level_label = arial_font.render("LEVEL 3", 1, (255, 255, 255))
        return level_label

    def animation(self, background_colour, board, board_disp, folder, level_label, screen):
        """Makes animation for 3 level."""
        chicken = Chicken()
        chicken.set_tile_center([600.5, 350])
        chicken_image = pygame.image.load(os.path.join(folder, "chickenFront.png"))
        self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)
        moves_to_do = board.count_two_down_tiles([600.5, 350])
        moves = [moves_to_do[0], [600.5, 350], moves_to_do[1], [600.5, 350]]

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move, 2)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)

        for move in moves:
            self.make_animation_move(board, board_disp, chicken, move, 1)
            self.display_on_screen(background_colour, board_disp, chicken, chicken_image, level_label, screen)
