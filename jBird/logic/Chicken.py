import pygame

from jBird.utils.ScreenSize import Positions


class Chicken():
    def __init__(self):
        self.position = Positions.CHICKEN_INIT_POSITION.value
        self.direction = "INIT DOWN"


    def move(self, direction):
        print("Kurczak zjezdzasz w dol idioto")
        self.position[1] += 100


