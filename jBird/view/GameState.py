import pygame
from jBird.utils.ScreenSize import ScreenSize
pygame.init()

class GameState:
    def __init__(self):

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))



        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        myFont = pygame.font.SysFont("arial", 40)
        player = myFont.render("Player: ", 1, (0, 255, 0))
        screen.blit(player, (0,0) )


        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False