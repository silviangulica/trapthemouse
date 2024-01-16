import pygame


class Piece:
    """
    Piece class. This class will represent a piece on the board. It could be a mouse, a blocked piece or a available piece.
    """

    def __init__(self, value, x, y, image_path):
        """
        The main constructor of the piece.
        :param value: The value of the piece. 0 - Available, 1 - Blocked, 2 - Mouse.
        :param x: Position for the x-axis of the piece.
        :param y: Position for the y-axis of the piece.
        :param image_path: The path to the image of the piece.
        """
        self.value = value
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def set_value(self, value):
        """
        Set the value of the piece, and change the image of the piece.
        :param value: The value of the piece. 0 - Available, 1 - Blocked, 2 - Mouse.
        :return: None
        """
        self.value = value
        if self.value == 0:
            self.image = pygame.image.load("assets/piece.png")
        elif self.value == 2:
            self.image = pygame.image.load("assets/mouse.png")
        elif self.value == 1:
            self.image = pygame.image.load("assets/blocked-piece.png")

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def check_click(self, x, y):
        """
        Check if the piece is clicked. This method will check if the mouse pos 
        is inside the piece by check if the mouse is in the radius of the circle 
        from the center of the piece.
        :param x: Position for the x-axis of the mouse.
        :param y: Position for the y-axis of the mouse.
        :return: True if the piece is clicked, False otherwise.
        """
        if (x - self.x - 37.5) ** 2 + (y - self.y - 37.5) ** 2 <= 37.5 ** 2:
            return True
        return False
