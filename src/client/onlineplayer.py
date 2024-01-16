from player import Player

from network import Network


class OnlinePlayer(Player):
    """
    Online player class. This player will not modify the table of the game. The player will use the network to send commands to the server.
    """

    def __init__(self, screen, network, board):
        """
        Initializes the online player.
        :param screen: The screen to draw on.
        :param network: The network to send commands to the server.
        :param board: The board to be used.
        """
        super().__init__(screen)
        self.network: Network = network
        self.map_table(board)
        self.my_turn = False
        self.need_to_redraw = True
        self.game_won = False
        self.winner = False

    def map_table(self, table):
        """
        Map the table to the player.
        :param table: The table to be mapped.
        :return: None
        """
        for i in range(self.height):
            for j in range(self.width):
                self.pieces[i][j].set_value(table[i][j])

    def make_move(self, x, y):
        """
        Validate the move and send it to the server.
        :param x: The x coordinate of the move.
        :param y: The y coordinate of the move.
        :return: None
        """
        for i in range(self.height):
            for j in range(self.width):
                if self.pieces[i][j].check_click(x, y) and self.pieces[i][j].value == 0:
                    self.send_move(i, j)

    def send_move(self, x, y):
        """
        Send the move to the server, without waiting for a response.
        :param x: The x coordinate of the move.
        :param y: The y coordinate of the move.
        :return: None
        """
        self.network.send_without_response(f"move:{x}:{y}")

    def check_online_table_and_win_status(self):
        """
        Check the online table and win status.
        :return: None
        """
        data = self.network.send("get_table")
        if data:
            self.map_table(data["table"])
            self.game_won = data["game_won"]
            self.winner = data["winner"]
            self.my_turn = data["my_turn"]
