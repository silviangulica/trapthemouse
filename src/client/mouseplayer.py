import random


class MousePlayer:
    """
    The mouse player of the game. 
    By default, the mouse is controlled by AI, but it can be controlled by a human player, locally or remotely.
    """

    def __init__(self, x, y, difficulty):
        """
        Initializes the mouse player.
        :param x: The x index of the mouse.
        :param y: The y index of the mouse.
        :param difficulty: The difficulty of the mouse. 0 - Easy, 1 - Medium, 2 - Hard.
        """
        self.x = x
        self.y = y
        self.difficulty = difficulty

    def make_move(self, board):
        """
        Makes a move for the mouse.
        :param board: The board, which is a 2D array.
        :return: Return 1 if the mouse is trapped, 0 if the mouse has escaped.
        """
        old_x = self.x
        old_y = self.y
        if self.difficulty >= 1:
            self.y, self.x = self.bfs(board)
        elif self.difficulty == 0:
            self.y, self.x = self.gen_random_move(board)

        print(f"Mouse moved to y={self.y} and x={self.x}")

        if self.x == -1 and self.y == -1:
            return 0
        if self.x == old_x and self.y == old_y:
            return 1

        board[old_y][old_x].set_value(0)
        board[self.y][self.x].set_value(2)

    def in_bounds(self, y, x, board):
        """
        Checks if the given (y, x) index is in bounds of the board.
        :param y: The y index of the cell.
        :param x: The x index of the cell.
        :param board: The board, which is a 2D array.
        :return: True if the cell is in bounds, False otherwise.
        """
        return 0 <= y < len(board) and 0 <= x < len(board[0])

    def gen_random_move(self, board):
        """
        Generates a random move for the mouse.
        :param board: The board, which is a 2D array.
        :return: The (y, x) index of the cell that the mouse should move.
        """
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

        if self.y % 2 == 0:
            directions = directions_even_row
        else:
            directions = directions_odd_row

        random.shuffle(directions)

        for direction in directions:
            new_y = self.y + direction[0]
            new_x = self.x + direction[1]

            if self.in_bounds(new_y, new_x, board) and board[new_y][new_x].value == 0:
                return new_y, new_x
            elif not self.in_bounds(new_y, new_x, board):
                return -1, -1

        return self.y, self.x

    def bfs(self, board):
        """
        Uses BFS to find the shortest path for the mouse to escape. 
        Because the table is in a hexagonal shape, the mouse can move in 6 directions.
        So on every even row, the mouse move in a direction, and viceversa.
        :param board: The board, which is a 2D array.
        :return: The (y, x) index of the cell that the mouse should move.
        """
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

        queue = [(self.y, self.x)]
        visited = {(self.y, self.x): None}

        y, x = 0, 0

        while queue:
            y, x = queue.pop(0)

            if self.difficulty == 1 and len(visited) > 15:
                return self.backtrack((y, x), visited, 1)

            if y % 2 == 0:
                directions = directions_even_row
            else:
                directions = directions_odd_row

            for direction in directions:
                new_y = y + direction[0]
                new_x = x + direction[1]

                if self.in_bounds(new_y, new_x, board) and (new_y, new_x) not in visited and board[new_y][new_x].value == 0:
                    visited[(new_y, new_x)] = (y, x)
                    queue.append((new_y, new_x))
                elif not self.in_bounds(new_y, new_x, board):
                    return self.backtrack((y, x), visited, 1)

        return self.backtrack((y, x), visited, 2)

    def backtrack(self, end, visited, called_from=0):
        """
        Backtracks from the end position to the second last position. So that the mouse can know where to go.
        :param end: The end position
        :param visited: The visited dictionary
        :param called_from: Default is 0. If needed, it can be set for a specific value that will represent moment of the BFS when is called. 1. From a position where mouse can escape. 2. From a position where mouse is trapped.
        :return: The (y, x) index of the cell that the mouse should move.
        """
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = visited[current]

        if len(path) == 1:
            if called_from == 1:
                return -1, -1
            elif called_from == 2:
                return self.y, self.x

        return path[-2][0], path[-2][1]
