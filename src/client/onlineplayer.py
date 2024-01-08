from player import Player
from _thread import *


class OnlinePlayer(Player):
    def __init__(self, screen, network, board):
        super().__init__(screen)
        self.network = network
        self.map_table(board)
        self.ready_to_make_move = False

    def map_table(self, table):
        print(table)
        for i in range(self.height):
            for j in range(self.width):
                self.pieces[i][j].set_value(table[i][j])

    def make_move(self, x, y):
        if self.ready_to_make_move:
            for i in range(self.height):
                for j in range(self.width):
                    if self.pieces[i][j].check_click(x, y) and self.pieces[i][j].value == 0:
                        self.network.send(f"move:{i}:{j}")
