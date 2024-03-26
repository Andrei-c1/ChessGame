import pygame

from const import *
from board import *
from dragger import *
class Game:

    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()


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

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):

                if self.board.squares[row][col].has_piece():

                    piece = self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                      img = pygame.image.load(piece.texture)
                      img_center = col * SQUARESIZE + SQUARESIZE // 2, row * SQUARESIZE + SQUARESIZE // 2
                      piece.text_rect = img.get_rect(center = img_center)
                      surface.blit(img, piece.text_rect)




