import pygame

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

table_piece = pygame.image.load("hexagon.png")

running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE
    screen.fill(pygame.Color("darkgrey"))
    screen.blit(table_piece, (int(screen.get_width() / 2)-48, 100))
    screen.blit(table_piece, (int(screen.get_width() / 2)-48+36, 100+48))
    screen.blit(table_piece, (int(screen.get_width() / 2)-48, 100+48+48))
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
