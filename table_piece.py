class TablePiece:
    def __init__(self, value, x, y):
        self.value = value
        self.x = x
        self.y = y

    def set_value(self, value):
        self.value = value

    def set_x(self, value):
        if value >= 0:
            self.x = value

    def set_y(self, value):
        if value >= 0:
            self.y = value

    def get_value(self):
        return self.value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
