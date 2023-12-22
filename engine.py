import pygame


class Engine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = True
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.game_objects = []

    def add_object_to_render(self, new_object):
        self.game_objects.append(new_object)

    def render(self):
        pygame.init()

        for game_object in self.game_objects:
            game_object.start()

        while self.running:
            self.screen.fill(pygame.Color(255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                for game_object in self.game_objects:
                    game_object.event_handler(event)

            for game_object in self.game_objects:
                game_object.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
