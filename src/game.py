import pygame

from piece import Piece


class Game:
    def __init__(self):
        self.board = []
        self.screen = None
        self.clock = None
        self.running = True
        self.piece_image = pygame.image.load("assets/piece.png")
        self.mouse_image = pygame.image.load("assets/mouse.png")
        self.mouse_image = pygame.transform.scale(self.mouse_image, (64, 64))
        self.offset_x = 0
        self.offset_y = 0
        self.margin_x = 70
        self.margin_y = 60
        self.player_turn = 1

    def start_game(self):
        self.screen = pygame.display.set_mode((1024, 720), pygame.RESIZABLE)
        self.offset_x = (self.screen.get_width() - 560) / 2
        self.offset_y = (self.screen.get_height() - 560) / 2
        self.clock = pygame.time.Clock()
        self.construct_board()

    def construct_board(self):
        for row in range(8):
            self.board.append([])
            for col in range(8):
                if row % 2 == 0:
                    self.board[row].append(Piece(
                        0, col * self.margin_x + self.offset_x, row * self.margin_y + self.offset_y))
                elif row % 2 == 1:
                    self.board[row].append(Piece(
                        0, col * self.margin_x + int(self.margin_x / 2) + self.offset_x,
                           row * self.margin_y + self.offset_y))

        self.board[0][0].set_value(2)

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                if self.board[row][col].value == 0:
                    self.screen.blit(
                        self.piece_image, (self.board[row][col].x, self.board[row][col].y))
                if self.board[row][col].value == 2:
                    self.screen.blit(
                        self.mouse_image, (self.board[row][col].x, self.board[row][col].y))

    def make_move(self, event_list):
        if self.player_turn == 1:
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    min_dist = 100000
                    min_row = -1
                    min_col = -1
                    for row in range(8):
                        for col in range(8):
                            if self.board[row][col].value == 0:
                                dist = ((pos[0] - (self.board[row][col].x + 16)) ** 2 +
                                        (pos[1] - (self.board[row][col].y + 16)) ** 2) ** 0.5
                                if dist < min_dist:
                                    min_dist = dist
                                    min_row = row
                                    min_col = col
                    self.board[min_row][min_col].set_value(1)
                    self.player_turn = 1
        elif self.player_turn == 2:
            pass

    def run_game(self):
        pygame.init()

        while self.running:
            self.screen.fill(pygame.Color(255, 255, 255))

            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.running = False

            self.make_move(event_list)

            self.draw_board()
            pygame.display.flip()
            self.clock.tick(60)

    def verify_win(self):
        pass
