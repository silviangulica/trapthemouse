from piece import Piece
import random
from player import Player


class TablePlayer(Player):
    def __init__(self, screen):
        super().__init__(screen)

    def make_piece_mouse(self, mouse):
        """
        Make a piece for the mouse.
        :param mouse: The mouse to make the piece for.
        :return: None
        """
        self.pieces[mouse.y][mouse.x] = Piece(
            2, mouse.x, mouse.y, "assets/mouse.png")

    def add_random_blocked_pieces(self):
        """
        Add random blocked pieces to the board.
        :return: None
        """
        for i in range(self.height):
            for j in range(self.width):
                random_number_to_devide = random.randint(0, (i + j) + 1) + 1
                if random_number_to_devide % random.randint(2, 9) == 0:
                    self.pieces[i][j].set_value(1)
