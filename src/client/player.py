from piece import Piece


class Player:
    """
    Player class. By defaut the player is a player that will 
    modify the table of the game. 
    """

    def __init__(self, screen):
        self.height = 9
        self.width = 8
        self.screen = screen
        self.pieces = [[Piece(0, 0, 0, "assets/piece.png")
                        for _ in range(self.width)] for _ in range(self.height)]

    def draw(self):
        """
        Draw the pieces on the screen.
        :param screen: The screen to draw on.
        :return: None
        """
        matrix_width = self.width * 75
        matrix_height = self.height * 75

        start_x = self.screen.get_width() / 2 - matrix_width / 2
        start_y = self.screen.get_height() / 2 - matrix_height / 2

        for i in range(self.height):
            for j in range(self.width):
                if i % 2 == 0:
                    self.pieces[i][j].set_x(start_x + j * 75)
                    self.pieces[i][j].set_y(start_y + i * 55)
                else:
                    self.pieces[i][j].set_x(start_x + j * 75 + 37.5)
                    self.pieces[i][j].set_y(start_y + i * 55)

                self.screen.blit(
                    self.pieces[i][j].image, (self.pieces[i][j].x, self.pieces[i][j].y))

    def make_move(self, x, y):
        """
        Make a move.
        :return: True if the move was made, False otherwise.
        """
        for row in self.pieces:
            for piece in row:
                if piece.check_click(x, y) and piece.value == 0:
                    piece.set_value(1)
                    return True
        return False
