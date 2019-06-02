"""The main game"""

import pygame
from pygame.locals import *
from config import *
from Player import Player
from Enemy import Enemy

# game initialization
pygame.init()
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('YoRHa-Manic')
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background.fill(BLACK)

ADDENEMY = pygame.USEREVENT +1 
pygame.time.set_timer(ADDENEMY,1000)

player = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    #screen.fill(BLACK)
    screen.blit(background, (0, 0))

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)  

    enemies.update()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    col = pygame.sprite.spritecollideany(player, enemies)
    if col != None:
        col.kill()
        if player.hp > 0:
            player.hp -= 1
        else:
            player.kill()

    pygame.display.flip()
    #clock.tick(FPS)
