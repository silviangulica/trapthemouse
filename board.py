import pygame

from gameobject import GameObject
from table_piece import TablePiece


class Board(GameObject):
    def __init__(self, width, height):
        """
        The board of the game.
        :param width: The width of the board. Default is 10.
        :param height: The height of the board. Default is 10.
        """
        self.width = width
        self.height = height
        self.board = []
        self.piece_img = pygame.image.load("hexagon.png")

    def draw(self, screen):
        for row in self.board:
            for piece in row:
                if piece.get_value() == 0:
                    screen.blit(self.piece_img, (piece.get_x(), piece.get_y()))

    def update(self):
        pass

    def start(self):
        self.board = [[TablePiece(0, 0, 0) for _ in range(self.width)] for _ in range(self.height)]

        x = 20
        y = 20
        even_row = True
        for row in self.board:
            for piece in row:
                piece.set_x(x)
                piece.set_y(y)
                x += 67
            if even_row:
                x = 55
            else:
                x = 20
            even_row = not even_row
            y += 55

    def event_handler(self, events):
        pass
