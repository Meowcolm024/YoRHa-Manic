"""The main game"""

import pygame
from pygame.locals import *
from config import *
from Player import Player


pygame.init()
screen = pygame.display.set_mode(windowSize)
player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

    screen.blit(player.image, (100, 100))
    pygame.display.flip()
