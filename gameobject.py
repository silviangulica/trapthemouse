class GameObject:
    def draw(self, screen):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def event_handler(self, events):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError
