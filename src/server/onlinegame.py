class OnlineGame:
    def __init__(self, game_id, player1, player2, game_type):
        self.game_id = game_id
        self.player1 = player1
        self.player2 = player2
        self.game_type = game_type
        self.table = [[0 for _ in range(9)] for _ in range(8)]
