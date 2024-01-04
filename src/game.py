import pygame

from button import Button


class Game:
    """
    The game class. which will launch the game with specific parameters.
    By default, the game will use a 8x8 grid.
    """

    def __init__(self):
        self.screen = None
        self.clock = pygame.time.Clock()

    def initialize_game(self):
        """
        Initializes the game with the configuration defined in constructor.
        :return: None
        """
        self.screen = pygame.display.set_mode((1024, 720), pygame.RESIZABLE)
        pygame.init()
        pygame.display.set_caption("Trap The Mouse")

    def main_menu(self):
        """
        The main menu for the game. TODO CONTINUE
        :return:
        """
        button_start_game = Button(self.screen, 50, 400, 200, 100, "Start Game",
                                   pygame.font.SysFont("Arial", 20), True, False)
        button_quit = Button(self.screen, 50, 550, 200, 100, "Quit",
                             pygame.font.SysFont("Arial", 20), True, False)

        menu_buttons = [button_start_game, button_quit]

        while True:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((68, 117, 28))

            for button in menu_buttons:
                button.draw()
                button.check_hover(mouse_pos[0], mouse_pos[1])

            # Check if the mouse is on the button
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_start_game.check_click(mouse_pos[0], mouse_pos[1]):
                        self.start_local_game()
                    if button_quit.check_click(mouse_pos[0], mouse_pos[1]):
                        pygame.quit()
                        quit()

            pygame.display.update()
            self.clock.tick(60)

    def start_local_game(self):
        """
        Start a local game with the default configuration.
        :return: None
        """
