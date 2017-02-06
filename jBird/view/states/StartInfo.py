import os
import sys

import pygame
from pygame.constants import MOUSEBUTTONDOWN
from pygame.constants import KEYDOWN

from jBird.utils.Constants import ScreenSize
from jBird.view.entities_and_widgets import Buttons
from jBird.view.states.GameState import GameState

pygame.init()
class StartInfo():
    """Info which appears when the game starts."""
    def __init__(self):
        """Initialization of StartInfo."""
        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        my_font_instr = pygame.font.SysFont("monospace", 50, True)

        label_instr = my_font_instr.render("Instructions", 1, (255, 255, 255))
        label_instr_rect = label_instr.get_rect(center=(width / 2, 60))
        screen.blit(label_instr, label_instr_rect)

        my_font_text = pygame.font.SysFont("monospace", 20, True)

        l1 = my_font_text.render("Welocome to J-bird Game!" , 1, (255, 255, 255))
        rect1 = l1.get_rect(center=(width / 2, 90))
        # screen.blit(l1, rect1)

        l2 = my_font_text.render("Moves:" , 1, (255, 255, 255))
        rect2 = l2.get_rect(center=(width / 2, 120))
        screen.blit(l2, rect2)

        l3 = my_font_text.render("up - left   : 7" , 1, (255, 255, 255))
        rect3 = l3.get_rect(center=(width / 2, 150))
        screen.blit(l3, rect3)

        l4 = my_font_text.render("up - right  : 9", 1, (255, 255, 255))
        rect4 = l4.get_rect(center=(width / 2, 180))
        screen.blit(l4, rect4)

        l5 = my_font_text.render("down - left : 1", 1, (255, 255, 255))
        rect5 = l5.get_rect(center=(width / 2, 210))
        screen.blit(l5, rect5)

        l6 = my_font_text.render("down - right: 3", 1, (255, 255, 255))
        rect6 = l6.get_rect(center=(width / 2, 240))
        screen.blit(l6, rect6)

        l7 = my_font_text.render("or", 1, (255, 255, 255))
        rect7 = l7.get_rect(center=(width / 2, 270))
        screen.blit(l7, rect7)

        l8 = my_font_text.render("up - left   : 1", 1, (255, 255, 255))
        rect8 = l8.get_rect(center=(width / 2, 300))
        screen.blit(l8, rect8)

        l9 = my_font_text.render("up - right  : q", 1, (255, 255, 255))
        rect9 = l9.get_rect(center=(width / 2, 330))
        screen.blit(l9, rect9)

        l10 = my_font_text.render("down - left : =", 1, (255, 255, 255))
        rect10 = l10.get_rect(center=(width / 2, 360))
        screen.blit(l10, rect10)

        l11 = my_font_text.render("down - right: p", 1, (255, 255, 255))
        rect11 = l11.get_rect(center=(width / 2, 390))
        screen.blit(l11, rect11)

        l12 = my_font_text.render("The bird earns the points by changing the color of the tiles.", 1, (255, 255, 255))
        rect12 = l12.get_rect(center=(width / 2, 420))
        screen.blit(l12, rect12)

        l13 = my_font_text.render("The birds dies when collides with ball or with snake.", 1, (255, 255, 255))
        rect13 = l13.get_rect(center=(width / 2, 450))
        screen.blit(l13, rect13)

        l14 = my_font_text.render("It also dies when falls from the piramid.", 1, (255, 255, 255))
        rect14 = l14.get_rect(center=(width / 2, 480))
        screen.blit(l14, rect14)

        l20 = my_font_text.render("Press any key to start a game", 1, (255, 255, 255))
        rect12 = l20.get_rect(center=(width / 2, 650))
        screen.blit(l20, rect12)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    newGameState = GameState()