import pygame
import sys

from const import *
from game import Game
class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("CHESS")
        self.game = Game()

    def mainLoop(self):

        while True:
            self.game.show_background(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()



main = Main()
main.mainLoop()
