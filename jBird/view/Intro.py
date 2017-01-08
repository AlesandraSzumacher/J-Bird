import pygame
from pygame.constants import MOUSEBUTTONDOWN

from jBird.utils.ScreenSize import ScreenSize
from jBird.view import Buttons
from jBird.view.GameState import GameState

pygame.init()

class Intro:
    def __init__(self):
        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('J-Bird')

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        myFont = pygame.font.SysFont("arial", 80)
        mainTextLabel = myFont.render("J-BIRD", 1, (0, 255, 0))

        imageJBird = pygame.image.load("jbird.png")
        screen.blit(imageJBird, (10, 20))

        screen.blit(mainTextLabel, (520, 20))

        # inputTextBox = InputText("Name")
        # [screen, textFromBox] = inputTextBox.ask(screen)


        button1 = Buttons.Button()
        button1.create(screen, (107, 142, 35), height // 2, width // 2, 200, 100, 0, "NEW GAME", (255, 255, 255))

        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    if button1.pressed(pygame.mouse.get_pos()):
                        newGameState = GameState()

intro = Intro()
