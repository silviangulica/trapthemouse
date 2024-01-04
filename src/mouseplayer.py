class MousePlayer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def make_move(self, board):
        pass

    def in_bounds(self, y, x):
        return 0 <= y < 5 and 0 <= x < 9

    def bfs(self):

        board = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1]
        ]

        self.x = 7
        self.y = 1

        start_cell = (self.y, self.x)
        neighbors = [[start_cell, None]]
        visited = {}
        directions = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
            [1, 1],
            [-1, -1],
            [1, -1],
            [-1, 1],
        ]

        while neighbors:
            current = neighbors.pop(0)
            visited.update({current[0]: current[1]})
            current = current[0]
            last_cell = current
            for direction in directions:
                new_y = current[0] + direction[0]
                new_x = current[1] + direction[1]
                if self.in_bounds(new_y, new_x):
                    if board[new_y][new_x] == 0 and (new_y, new_x) not in visited:
                        neighbors.append([(new_y, new_x), last_cell])
                elif not self.in_bounds(new_y, new_x) and board[current[0]][current[1]] == 0:
                    cell = last_cell
                    while visited[visited[cell]] is not None:
                        cell = visited[cell]
                    return cell
