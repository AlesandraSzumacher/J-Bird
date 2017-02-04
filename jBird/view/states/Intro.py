import os
import sys

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from jBird.utils.Constants import ScreenSize
from jBird.view.entities_and_widgets import Buttons
from jBird.view.states.GameState import GameState

pygame.init()

class Intro:
    def __init__(self):
        folder = os.path.dirname(os.path.realpath(__file__))

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('J-Bird')

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        imageJBird = pygame.image.load(os.path.join(folder, "jbirdnapis.png"))
        imageJBirdWidth = imageJBird.get_rect().size[0]
        screen.blit(imageJBird, (width/2 - imageJBirdWidth/2, 20))

        button1 = Buttons.Button()
        button1height = 200
        button1width = 100
        button1.create(screen, (176, 54, 82), width/2 - button1width, height // 2 + button1height, 200, 100, 0, "NEW GAME", (255, 255, 255))

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    if button1.pressed(pygame.mouse.get_pos()):
                        newGameState = GameState()

intro = Intro()
