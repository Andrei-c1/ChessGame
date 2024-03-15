from const import *
from square import *


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0]for col in range(COLS)]

        self._create()

    def _create(self):
        for col in range(COLS):
            for row in range(ROWS):
                self.squares = Square(row, col)


    def __add_pieces(self, color):
        pass
