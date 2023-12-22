# import pygame
#
# # Setup pygame
# pygame.init()
# running = True
# screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# clock = pygame.time.Clock()
#
# # Setup table
# while running:
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     pygame.display.flip()
#
#     clock.tick(60)
#
# pygame.quit()
from board import Board
from engine import Engine

engine = Engine(1280, 720)

board = Board(10, 10)
engine.add_object_to_render(board)

engine.render()  # The last function on engine configuration
