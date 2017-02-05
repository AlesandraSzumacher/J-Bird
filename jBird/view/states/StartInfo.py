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
    def __init__(self):
        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        myfont = pygame.font.SysFont("monospace", 50, True)

        label = myfont.render("Instructions", 1, (255, 255, 255))
        text_rect = label.get_rect(center=(width / 2, 60))
        screen.blit(label, text_rect)

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                elif event.type == KEYDOWN:
                    newGameState = GameState()