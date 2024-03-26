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

        board = self.game.board
        dragger = self.game.dragger

        while True:
            self.game.show_background(self.screen)
            self.game.show_pieces(self.screen)

            if dragger.dragging:
                dragger.update_blit(self.screen)

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQUARESIZE
                    clicked_col = dragger.mouseX // SQUARESIZE

                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)

                elif event.type == pygame.MOUSEMOTION:
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        self.game.show_background(self.screen)
                        self.game.show_pieces(self.screen)
                        dragger.update_blit(self.screen)

                elif event.type == pygame.MOUSEBUTTONUP:
                    dragger.undrag_piece()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainLoop()
