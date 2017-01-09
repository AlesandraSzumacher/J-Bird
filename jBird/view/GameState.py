import pygame
import pygame.constants
from pygame.constants import MOUSEBUTTONDOWN

from jBird.logic.Game import Game
from jBird.utils.ScreenSize import ScreenSize, TileColor
from jBird.view.BoardDisplayer import BoardDisplay

pygame.init()


class GameState:
    def __init__(self):
        game = Game()

        (width, height) = (ScreenSize.WIDTH.value, ScreenSize.HEIGHT.value)
        screen = pygame.display.set_mode((width, height))

        background_colour = (0, 0, 0)
        screen.fill(background_colour)

        arialFont = pygame.font.SysFont("arial", 40)
        player = arialFont.render("Player: ", 1, (0, 255, 0))
        screen.blit(player, (0, 0))
        '''
        rhH = 25
        rhW = 40
        rhombus = Rhombus(rhH, rhW)
        rhombus.create(screen, (0,0,255), (width // 2 + 1 - rhW, 200))
        '''
        boardDis = BoardDisplay(game.board)

        boardDis.displayBoard(screen)
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    for tile in boardDis.tileRhombusList:
                        if tile.tile.pressed(pygame.mouse.get_pos()):
                            tile.changeColor((0,255,0))
                            break
                    '''
                    for i in range(len(boardDis.tileRhombusList)):
                        if boardDis.tileRhombusList[i].tile.pressed(pygame.mouse.get_pos()):
                            boardDis.tileRhombusList[i].changeColor((0, 255, 0))
                            break
                    '''
                    boardDis.displayBoard(screen)
                    pygame.display.flip()
                    print("done")


GameState()
