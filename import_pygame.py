"""The first lesson using pygame."""

import pygame
from sys import exit

# initiate pygame
pygame.init()
# display screen
screen = pygame.display.set_mode((800, 400))

while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

