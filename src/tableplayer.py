from piece import Piece


class TablePlayer:
    def __init__(self, screen, width, height):
        self.height = height
        self.width = width
        self.screen = screen
        self.pieces = [[None for _ in range(width)] for _ in range(height)]

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
                if self.pieces[i][j] is not None:
                    if i % 2 == 0:
                        self.pieces[i][j].set_x(start_x + j * 75)
                        self.pieces[i][j].set_y(start_y + i * 75)
                    else:
                        self.pieces[i][j].set_x(start_x + j * 75 + 37.5)
                        self.pieces[i][j].set_y(start_y + i * 75)
                else:
                    if i % 2 == 0:
                        self.pieces[i][j] = Piece(
                            0, start_x + j * 75, start_y + i * 75, "assets/piece.png")
                    else:
                        self.pieces[i][j] = Piece(
                            0, start_x + j * 75 + 37.5, start_y + i * 75, "assets/piece.png")

                self.screen.blit(
                    self.pieces[i][j].image, (self.pieces[i][j].x, self.pieces[i][j].y))

    def make_move(self, x, y):
        """
        Make a move.
        :return: None
        """
        for row in self.pieces:
            for piece in row:
                if piece.check_click(x, y):
                    piece.set_value(1)

    def make_piece_mouse(self, mouse):
        """
        Make a piece for the mouse.
        :param mouse: The mouse to make the piece for.
        :return: None
        """
        self.pieces[mouse.y][mouse.x] = Piece(
            2, mouse.x, mouse.y, "assets/mouse.png")
