from player import Player
from _thread import *

from network import Network


class OnlinePlayer(Player):
    def __init__(self, screen, network, board):
        super().__init__(screen)
        self.network: Network = network
        self.map_table(board)
        self.my_turn = False
        self.need_to_redraw = True
        self.game_won = False
        self.winner = False

    def map_table(self, table):
        for i in range(self.height):
            for j in range(self.width):
                self.pieces[i][j].set_value(table[i][j])

    def make_move(self, x, y):
        for i in range(self.height):
            for j in range(self.width):
                if self.pieces[i][j].check_click(x, y) and self.pieces[i][j].value == 0:
                    self.send_move(i, j)

    def send_move(self, x, y):
        self.network.send_without_response(f"move:{x}:{y}")

    def check_online_table_and_win_status(self):
        data = self.network.send("get_table")
        if data:
            self.map_table(data["table"])
            self.game_won = data["game_won"]
            self.winner = data["winner"]
            self.my_turn = data["my_turn"]
