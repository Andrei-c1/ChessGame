import os


class Piece:

    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.moves = []
        self.moved = False
        self.name = name
        self.color = color
        self.value = value
        self.texture = texture
        self.set_texture()
        self.text_rect = texture_rect

    def set_texture(self):
        self.texture = os.path.join(
            f'assets/images/imgs/{self.color}_{self.name}.png'
        )

    def add_moves(self, move):
        self.moves.append(move)


class Pawn(Piece):

    def __init__(self, color):
        self.direction = -1 if color == 'white' else 1
        super().__init__('pawn', color, 1)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color, 3)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color, 3)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color, 5)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color, 9)


class King(Piece):

    def __init__(self, color):
        super().__init__('king', color, 10000)
