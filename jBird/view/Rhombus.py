import pygame
from pygame import gfxdraw

class Rhombus:
    def __init__(self, h = 5, w = 10):
        self.h = 30
        self.w = 50

    def create(self, screen, color, leftCoordinates):
        screen = self.draw_rhombus(screen, color, leftCoordinates)

    def draw_rhombus(self, screen, color, leftCoordinate):
        upCoordinate = [leftCoordinate[0] + self.w, leftCoordinate[1] - self.h]
        downCoordinate = [leftCoordinate[0] + self.w, leftCoordinate[1] + self.h]
        rightCoordinate = [leftCoordinate[0] + self.w * 2, leftCoordinate[1]]
        listOfCoordinates = [leftCoordinate, upCoordinate, rightCoordinate, downCoordinate]
        pygame.gfxdraw.filled_polygon(screen, listOfCoordinates, (255,0,0))
        return screen

