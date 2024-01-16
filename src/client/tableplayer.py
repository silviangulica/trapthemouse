from piece import Piece
import random
from player import Player


class TablePlayer(Player):
    """
    TablePlayer class. This class will represent a player that will modify the table of the game.
    """

    def __init__(self, screen, difficulty):
        """
        Initializes the table player.
        :param screen: The screen to draw on.
        :param difficulty: The difficulty of the game, from 0(Easy) to 2(Hard).
        """
        super().__init__(screen)
        self.difficulty = difficulty

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
        maximum_pieces = 1
        minimum_pieces = 1
        if self.difficulty == 0:
            maximum_pieces = 25
            minimum_pieces = 15
        elif self.difficulty == 1:
            maximum_pieces = 10
            minimum_pieces = 5
        elif self.difficulty == 2:
            maximum_pieces = 5

        random_pieces = random.randint(minimum_pieces, maximum_pieces)
        for i in range(random_pieces):
            while True:
                random_x = random.randint(0, self.width - 1)
                random_y = random.randint(0, self.height - 1)
                if self.pieces[random_y][random_x].value == 0:
                    self.pieces[random_y][random_x].set_value(1)
                    break
