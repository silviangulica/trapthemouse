import pygame


class Button:
    """
    This class will implement buttons in the game.
    """

    def __init__(self, screen, x, y, width, height, text, font, lock_x, lock_y, color="#ffffff", hover_color="#E84F2E"):
        """
        The main constructor of the button.
        :param x: Position for the x-axis of the button.
        :param y: Position for the y-axis of the button.
        :param width: Width of the button.
        :param height: Height of the button.
        :param text: Text of the button.
        :param color: Color of the button, default color is white.
        :param hover_color: Color of the button on hover mode, default color is red(#E84F2E).
        """
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.screen = screen
        self.y_offset = screen.get_height() - self.y
        self.x_offset = screen.get_width() - self.x
        self.text = text
        self.font = font
        self.color = color
        self.hover_color = hover_color
        self.lock_y = lock_y
        self.lock_x = lock_x

    def draw(self):
        """
        Draw the button on the screen. It will resize the button based on the screen size.
        :return: None
        """
        if not self.lock_y:
            self.y = self.screen.get_height() - self.y_offset
        if not self.lock_x:
            self.width = self.screen.get_width() - self.x_offset
        pygame.draw.rect(self.screen, self.color,
                         (self.x, self.y, self.width, self.height))
        text = self.font.render(self.text, True, (0, 0, 0))
        self.screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                                self.y + (self.height / 2 - text.get_height() / 2)))

    def check_click(self, x, y):
        """
        Check if the button is clicked.
        :param x: Position for the x-axis of the mouse.
        :param y: Position for the y-axis of the mouse.
        :return: True if the button is clicked, False otherwise.
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                return True
        return False

    def check_hover(self, x, y):
        """
        Check if the mouse is on the button.
        :param x: Position for the x-axis of the mouse.
        :param y: Position for the y-axis of the mouse.
        :return: None
        """
        if self.x <= x <= self.x + self.width:
            if self.y <= y <= self.y + self.height:
                self.color = self.hover_color
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                return True
        self.color = "#ffffff"
        return False
