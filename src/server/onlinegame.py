import random


class OnlineGame:
    def __init__(self, game_id, player1, player2):
        self.game_id = game_id
        self.player1 = player1
        self.player2 = player2
        self.width = 8
        self.height = 9
        self.table = [[0 for _ in range(self.width)]
                      for _ in range(self.height)]
        self.game_started = False
        self.game_won = False
        self.player_to_move = 0
        self.piece_to_place = 1
        self.winner = None
        self.winner_name = ""

    def start_game(self):
        self.player_to_move = self.player1
        self.game_started = True
        random_x = random.randint(4, self.width - 3)
        random_y = random.randint(4, self.height - 3)
        self.table[random_y][random_x] = 2

        # place random pieces on the table
        random_pieces = random.randint(10, 15)
        for i in range(random_pieces):
            while True:
                random_x = random.randint(0, self.width - 1)
                random_y = random.randint(0, self.height - 1)
                if self.table[random_y][random_x] == 0:
                    self.table[random_y][random_x] = 1
                    break

    def make_move(self, player, y, x):
        if self.game_started and self.table[y][x] == 0:
            if self.player_to_move == self.player1 and player == self.player1:
                self.player_to_move = self.player2
                self.table[y][x] = 1

                if self.table_won():
                    self.end_game(self.player1)

            elif self.player_to_move == self.player2 and player == self.player2:
                directions = self.get_directions_for_mouse(y, x)
                for direction in directions:
                    if self.in_bounds(y + direction[0], x + direction[1]) and self.table[y + direction[0]][x + direction[1]] == 2:
                        self.table[y + direction[0]][x + direction[1]] = 0
                        self.table[y][x] = 2
                        self.player_to_move = self.player1
                        if self.mouse_won(y, x):
                            self.end_game(self.player2)
                        break

    def table_won(self):
        x, y = 0, 0
        for i in range(self.height):
            for j in range(self.width):
                if self.table[i][j] == 2:
                    y, x = i, j
                    break

        available_moves = self.get_available_moves(y, x)
        if available_moves == 0:
            self.end_game(self.player1)
            return True
        return False

    def get_available_moves(self, y, x):
        available_moves = 0
        directions = self.get_directions_for_mouse(y, x)
        for direction in directions:
            if self.in_bounds(y + direction[0], x + direction[1]) and self.table[y + direction[0]][x + direction[1]] == 0:
                available_moves += 1
        return available_moves

    def get_directions_for_mouse(self, y, x):
        directions_even_row = [
            [0, 1],     # Right
            [0, -1],    # Left
            [1, 0],     # Down
            [-1, 0],    # Up
            [-1, -1],   # Up Left
            [1, -1],    # Down Left
        ]
        directions_odd_row = [
            [0, 1],     # Right
            [0, -1],    # Left
            [1, 0],     # Down
            [-1, 0],    # Up
            [1, 1],     # Down Right
            [-1, 1],    # Up Right
        ]

        if y % 2 == 0:
            directions = directions_even_row
        else:
            directions = directions_odd_row

        return directions

    def end_game(self, winner):
        self.winner = winner
        self.game_won = True
        self.winner_name = "mouse" if winner == self.player2 else "table"

    def in_bounds(self, y, x):
        return 0 <= y < self.height and 0 <= x < self.width

    def mouse_won(self, y, x):
        result = 0 == y or self.height - 1 == y or 0 == x or self.width - 1 == x
        print(f"Checking if mouse won with y={y} and x={x} and {result}")
        return result
