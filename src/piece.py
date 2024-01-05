import pygame


class Piece:
    def __init__(self, value, x, y, image_path):
        self.value = value
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)

    def set_value(self, value):
        self.value = value

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
