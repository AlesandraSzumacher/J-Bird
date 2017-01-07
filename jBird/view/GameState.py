import pygame
from jBird.utils.ScreenSize import ScreenSize

(width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
screen = pygame.display.set_mode((width, height))

background_colour = (0, 0, 0)
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False