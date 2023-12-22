import game_modes


class Game:
    def __init__(self):
        self.game_mode = game_modes.GameModes.PLAYER_VS_PLAYER_LOCAL

    def start_game(self):
        pass

    def verify_win(self, player):
        pass

    def set_game_mode(self, game_mode):
        self.game_mode = game_mode
