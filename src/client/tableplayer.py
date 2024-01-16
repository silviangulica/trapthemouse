from piece import Piece
import random
from player import Player


class TablePlayer(Player):
    def __init__(self, screen, difficulty):
        super().__init__(screen)
        self.difficulty = difficulty + 1

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
        random_pieces = random.randint(
            int(10 / self.difficulty), int(15 / self.difficulty))
        for i in range(random_pieces):
            while True:
                random_x = random.randint(0, self.width - 1)
                random_y = random.randint(0, self.height - 1)
                if self.pieces[random_y][random_x].value == 0:
                    self.pieces[random_y][random_x].set_value(1)
                    break
