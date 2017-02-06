import os
import sys

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from jBird.utils.Constants import ScreenSize
from jBird.view.entities_and_widgets import Buttons
from jBird.view.states.StartInfo import StartInfo

pygame.init()


class Intro:
    """Class containing methods and attributes referring to Intro state."""

    def __init__(self):
        """Initialization of Intro state."""
        folder = os.path.dirname(os.path.realpath(__file__))

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('J-Bird')

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        imageJBird = pygame.image.load(os.path.join(folder, "jbirdnapis.png"))
        imageJBirdWidth = imageJBird.get_rect().size[0]
        screen.blit(imageJBird, (width / 2 - imageJBirdWidth / 2, 20))

        my_font_instr = pygame.font.SysFont("monospace", 30, True)

        label_instr = my_font_instr.render("By", 1, (255, 255, 255))
        label_instr_rect = label_instr.get_rect(center=(width / 2, 350))
        screen.blit(label_instr, label_instr_rect)

        label_instr = my_font_instr.render("Maria Babkiewicz", 1, (255, 255, 255))
        label_instr_rect = label_instr.get_rect(center=(width / 2, 400))
        screen.blit(label_instr, label_instr_rect)

        label_instr = my_font_instr.render("Aleksandra Szumacher", 1, (255, 255, 255))
        label_instr_rect = label_instr.get_rect(center=(width / 2, 440))
        screen.blit(label_instr, label_instr_rect)

        button1 = Buttons.Button()
        button1height = 200
        button1width = 100
        button1.create(screen, (176, 54, 82), width / 2 - button1width, height // 2 + button1height, 200, 100, 0,
                       "NEW GAME", (255, 255, 255))

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit(0)
                elif event.type == MOUSEBUTTONDOWN:
                    if button1.pressed(pygame.mouse.get_pos()):
                        newStartInfo = StartInfo()


intro = Intro()