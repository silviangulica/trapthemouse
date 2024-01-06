class MousePlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_move(self, board):
        old_x = self.x
        old_y = self.y
        self.y, self.x = self.bfs(board)
        board[old_y][old_x].set_value(0)
        board[self.y][self.x].set_value(2)
        print()
        print("Mouse moved to: ", self.y, self.x)
        for row in board:
            for piece in row:
                print(piece.value, end=" ")
            print()
        return self.y, self.x

    def in_bounds(self, y, x, board):
        return 0 <= y < len(board) and 0 <= x < len(board[0])

    def bfs(self, board):
        directions = [
            [0, 1],     # Right
            [0, -1],    # Left
            [1, 0],     # Down
            [-1, 0],    # Up
            [-1, -1],   # Up Left
            [1, -1],    # Down Left
        ]

        queue = [(self.y, self.x)]
        visited = {}
        visited[(self.y, self.x)] = None

        while queue:
            y, x = queue.pop(0)

            for direction in directions:
                new_y = y + direction[0]
                new_x = x + direction[1]

                if self.in_bounds(new_y, new_x, board) and (new_y, new_x) not in visited and board[new_y][new_x].value == 0:
                    visited[(new_y, new_x)] = (y, x)
                    queue.append((new_y, new_x))
                elif not self.in_bounds(new_y, new_x, board):
                    return self.backtrack((y, x), visited)

    def backtrack(self, end, visited):
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = visited[current]
        return path[-2][0], path[-2][1]
