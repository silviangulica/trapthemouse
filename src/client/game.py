import pygame
import pygame_gui
from button import Button
from mouseplayer import MousePlayer
from tableplayer import TablePlayer
from network import Network
from onlineplayer import OnlinePlayer


class Game:
    """
    The game class. which will launch the game with specific parameters.
    By default, the game will use a 8x8 grid.
    """

    def __init__(self):
        self.screen = None
        self.manager = None
        self.text_input = None
        self.clock = pygame.time.Clock()
        self.title_rect = None
        self.difficulty = 0

    def initialize_game(self):
        """
        Initializes the game with the configuration defined in constructor.
        :return: None
        """
        self.screen = pygame.display.set_mode(
            (1024, 720))
        pygame.init()
        self.manager = pygame_gui.UIManager((1024, 720))
        pygame.display.set_caption("Trap The Mouse")
        self.text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect(
            (300, 400), (200, 50)), manager=self.manager, object_id="#game_id")
        self.title_font = pygame.font.Font("freesansbold.ttf", 46)
        self.title_rect = self.title_font.render(
            f"Trap The Mouse", True, (0, 0, 0))

    def display_title(self):
        """
        Display the title of the game.
        :return: None
        """
        self.screen.blit(self.title_rect,
                         ((self.screen.get_width() - self.title_rect.get_width()) / 2,
                          self.title_rect.get_height() + 50))

    def main_menu(self):
        """
        The screen for main menu. It will display buttons for the user to choose.
        :return: None
        """
        button_online_game = Button(self.screen, 50, 250, 200, 100, "Online Game",
                                    pygame.font.SysFont("Arial", 20), True, False)
        button_start_game = Button(self.screen, 50, 400, 200, 100, "Start Game",
                                   pygame.font.SysFont("Arial", 20), True, False)
        button_quit = Button(self.screen, 50, 550, 200, 100, "Quit",
                             pygame.font.SysFont("Arial", 20), True, False)
        difficulty_button = Button(self.screen, 300, 400, 200, 100,
                                   "Difficulty: Easy", pygame.font.SysFont("Arial", 20), True, False)

        menu_buttons = [button_start_game, button_quit,
                        button_online_game, difficulty_button]

        while True:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((68, 117, 28))

            self.display_title()

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
                            if winner != "quit":
                                self.display_winner_info(winner)
                        elif button_quit.check_click(mouse_pos[0], mouse_pos[1]):
                            pygame.quit()
                            quit()
                        elif button_online_game.check_click(mouse_pos[0], mouse_pos[1]):
                            self.online_menu()
                        elif difficulty_button.check_click(mouse_pos[0], mouse_pos[1]):
                            self.difficulty = (self.difficulty + 1) % 3
                            if self.difficulty == 0:
                                difficulty_button.text = "Difficulty: Easy"
                            elif self.difficulty == 1:
                                difficulty_button.text = "Difficulty: Medium"
                            elif self.difficulty == 2:
                                difficulty_button.text = "Difficulty: Hard"

            pygame.display.update()
            self.clock.tick(60)

    def start_local_game(self):
        """
        Start a local game with the default configuration.
        :return: None
        """
        # When changing the windows, the cursor need to be reset
        pygame.mouse.set_cursor(*pygame.cursors.arrow)

        quit_button = Button(self.screen, 50, 550, 200, 100, "Quit",
                             pygame.font.SysFont("Arial", 20), True, False)

        buttons = [quit_button]

        game_end = False

        tableplayer = TablePlayer(self.screen, self.difficulty)
        tableplayer.add_random_blocked_pieces()
        mouseplayer = MousePlayer(4, 4, self.difficulty)

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

            for button in buttons:
                button.draw()
                button.check_hover(mouse_pos[0], mouse_pos[1])

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
                        if quit_button.check_click(mouse_pos[0], mouse_pos[1]):
                            return "quit"

                    # Debug only
                    elif event.button == 3:
                        tableplayer.make_move(mouse_pos[0], mouse_pos[1])

            pygame.display.update()
            self.clock.tick(60)

        return winner

    def display_winner_info(self, winner):
        """
        Display the winner information.
        :param winner: The winner of the game.
        :return: None
        """
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

    def online_menu(self):
        """
        Start an online game with the default configuration.
        :return: None
        """

        network = Network()
        connection_status = network.connect()

        if connection_status != "conn":
            print("Error connecting to the server.")
            return

        button_create_game = Button(self.screen, 50, 250, 200, 100, "Create Game",
                                    pygame.font.SysFont("Arial", 20), True, False)

        button_connect_game = Button(self.screen, 50, 400, 200, 100, "Connect Game",
                                     pygame.font.SysFont("Arial", 20), True, False)

        button_back = Button(self.screen, 50, 550, 200, 100, "Back",
                             pygame.font.SysFont("Arial", 20), True, False)

        button_set_game_id = Button(self.screen, 300, 250, 200, 100, "Set Game ID",
                                    pygame.font.SysFont("Arial", 20), True, False)

        menu_buttons = [button_create_game, button_back,
                        button_connect_game, button_set_game_id]

        winner = ""
        game_id = 0

        game_id_font = pygame.font.Font("freesansbold.ttf", 20)
        menu_info_font = pygame.font.Font("freesansbold.ttf", 20)
        menu_info_text = menu_info_font.render(
            f"\nGame ID -> Enter the game ID by typing the ID of the \n   game you want to play, confirm by pressing Enter.", True, (0, 0, 0))

        while True:
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((157, 204, 158))

            self.display_title()

            game_id_text = game_id_font.render(
                f"Game to connect:{game_id}", True, (0, 0, 0))

            self.screen.blit(game_id_text, (300, 400))
            self.screen.blit(menu_info_text, (300, 450))

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
                        if button_create_game.check_click(mouse_pos[0], mouse_pos[1]):
                            data = network.send("make_game:")
                            if data:
                                winner = self.start_online_game(network, data)
                        elif button_back.check_click(mouse_pos[0], mouse_pos[1]):
                            return
                        elif button_connect_game.check_click(mouse_pos[0], mouse_pos[1]):
                            data = network.send(f"join_game:{game_id}")
                            if data:
                                winner = self.start_online_game(network, data)
                        elif button_set_game_id.check_click(mouse_pos[0], mouse_pos[1]):
                            game_id = self.get_game_id_from_input()

            if winner == None:
                return
            elif winner != "":
                self.display_winner_info(winner)
                return

            pygame.display.update()
            self.clock.tick(60)

    def get_game_id_from_input(self):
        """
        Get the game id from the input box via the UI (PyGame UI).
        :return: The game id.
        """
        game_id = 0
        stop = False
        while not stop:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                    if event.ui_element == self.text_input:
                        try:
                            game_id = int(self.text_input.text)
                            stop = True
                        except:
                            pass

                self.manager.process_events(event)

            self.manager.update(1 / 60.0)
            self.manager.draw_ui(self.screen)
            pygame.display.update()
            self.clock.tick(60)

        return game_id

    def start_online_game(self, network, data):
        """
        Start an online game with the default configuration.
        :return: None
        """
        online_player = OnlinePlayer(self.screen, network, data["table"])
        quit_button = Button(self.screen, 50, 550, 200, 100, "Quit",
                             pygame.font.SysFont("Arial", 20), True, False)

        game_id_font = pygame.font.Font("freesansbold.ttf", 20)
        game_id_text = game_id_font.render(
            f"Game ID:{data['game_id']}", True, (0, 0, 0))

        buttons = [quit_button]
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        text_turn_font = pygame.font.Font("freesansbold.ttf", 20)

        while True:
            online_player.check_online_table_and_win_status()
            mouse_pos = pygame.mouse.get_pos()
            events = pygame.event.get()

            self.screen.fill((157, 204, 158))

            self.text_turn = "Your turn" if online_player.my_turn else "Opponent's turn"
            text_turn = text_turn_font.render(
                self.text_turn, True, (0, 0, 0))
            self.screen.blit(text_turn, (50, 100))
            self.screen.blit(game_id_text, (50, 50))
            online_player.draw()

            for button in buttons:
                button.draw()
                button.check_hover(mouse_pos[0], mouse_pos[1])

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        online_player.make_move(mouse_pos[0], mouse_pos[1])
                        if quit_button.check_click(mouse_pos[0], mouse_pos[1]):
                            return

            pygame.display.update()
            self.clock.tick(60)

            if online_player.game_won:
                break

        return online_player.winner
