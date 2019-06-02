"""The main game"""

import pygame
from pygame.locals import *
from config import *
from Player import Player


pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('YoRHa-Manic')
clock = pygame.time.Clock()

player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)  

    screen.fill(blackColor)
    
    screen.blit(player.image, (player.rect.centerx, player.rect.centery))

    pygame.display.flip()
    clock.tick(fps)
