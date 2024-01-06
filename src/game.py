import pygame

from button import Button
from mouseplayer import MousePlayer
from tableplayer import TablePlayer


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
        self.screen = pygame.display.set_mode(
            (1024, 720), pygame.RESIZABLE, pygame.SRCALPHA)
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

        title_font = pygame.font.Font("freesansbold.ttf", 46)
        title_rect = title_font.render(
            f"Trap The Mouse", True, (0, 0, 0))

        while True:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((68, 117, 28))

            self.screen.blit(title_rect,
                             ((self.screen.get_width() - title_rect.get_width()) / 2,
                              title_rect.get_height() + 50))

            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            for button in menu_buttons:
                button.draw()
                button.check_hover(mouse_pos[0], mouse_pos[1])

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_start_game.check_click(mouse_pos[0], mouse_pos[1]):
                            # All the game logic and different game screens
                            winner = self.start_local_game()
                            self.display_winner_info(winner)
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
        # When changing the windows, the cursor need to be reset
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

        game_end = False

        tableplayer = TablePlayer(self.screen, 8, 9)
        tableplayer.add_random_blocked_pieces()
        mouseplayer = MousePlayer(4, 4)

        tableplayer.make_piece_mouse(mouseplayer)
        table_player = True
        mouse_player = False
        player_to_move = table_player

        while not game_end:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((157, 204, 158))
            winner = "none"

            tableplayer.draw()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if player_to_move:  # PLAYER TABLE MOVE
                            if tableplayer.make_move(mouse_pos[0], mouse_pos[1]):
                                tableplayer.draw()
                                player_to_move = mouse_player
                        if not player_to_move:  # PLAYER MOUSE MOVE
                            mouseplayer_code = mouseplayer.make_move(
                                tableplayer.pieces)
                            if mouseplayer_code == 0:
                                game_end = True
                                winner = "mouse"
                            elif mouseplayer_code == 1:
                                game_end = True
                                winner = "table"
                            player_to_move = table_player

                    # Debug only
                    elif event.button == 3:
                        tableplayer.make_move(mouse_pos[0], mouse_pos[1])

            pygame.display.update()
            self.clock.tick(60)

        return winner

    def display_winner_info(self, winner):
        background = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        background.fill((175, 222, 166, 175))
        self.screen.blit(background, (0, 0))

        font_announcement = pygame.font.Font("freesansbold.ttf", 46)
        winner_announcement_rect = font_announcement.render(
            f"The winner is {winner.upper()}", True, (0, 0, 0))
        self.screen.blit(winner_announcement_rect,
                         ((self.screen.get_width() - winner_announcement_rect.get_width()) / 2,
                          winner_announcement_rect.get_height() + 50))

        back_button = Button(self.screen, (self.screen.get_width() - 200) / 2, 550, 200, 100, "Back",
                             pygame.font.SysFont("Arial", 20), True, False)
        while True:

            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            back_button.draw()
            back_button.check_hover(mouse_pos[0], mouse_pos[1])

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if back_button.check_click(mouse_pos[0], mouse_pos[1]):
                            return

            pygame.display.update()
            self.clock.tick(60)
