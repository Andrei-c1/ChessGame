import pygame

from const import *
class Game:

    def __init__(self):
        pass

    ################
    # SHOW METHODS #
    ################

    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = LIGHT_GREEN
                else:
                    color = DARK_GREEN

                rectangle = (col * SQUARESIZE, row * SQUARESIZE, SQUARESIZE, SQUARESIZE)
                pygame.draw.rect(surface, color, rectangle)

