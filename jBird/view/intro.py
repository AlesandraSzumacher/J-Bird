import pygame
pygame.init()

(width, height) = (800, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('J-Bird')

background_colour = (0, 0, 0)
screen.fill(background_colour)

myFont = pygame.font.SysFont("comicsansms", 100)
mainTextLabel = myFont.render("J-BIRD", 1, (0, 255, 0))

screen.blit(mainTextLabel, (520, 20))



pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
