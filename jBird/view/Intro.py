import pygame
from pygame.constants import MOUSEBUTTONDOWN

from jBird.utils import ScreenSize
from jBird.view import Buttons

pygame.init()

(width, height) = (800, 600)#(ScreenSize.WIDTH, ScreenSize.HEIGHT)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('J-Bird')

background_colour = (0, 0, 0)
screen.fill(background_colour)

myFont = pygame.font.SysFont("arial", 80)
mainTextLabel = myFont.render("J-BIRD", 1, (0, 255, 0))

screen.blit(mainTextLabel, (520, 20))

button1 = Buttons.Button()
button1.create(screen, (107,142,35), 225, 135, 200,    100,    0,        "Example", (255,255,255))

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            if button1.pressed(pygame.mouse.get_pos()):
                print("Cos sie stalo")
