"""The main game"""

import pygame
from pygame.locals import *
from config import *
from Player import Player
from Enemy import Enemy

# game initialization
pygame.init()
screen = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption('YoRHa-Manic')
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background.fill(BLACK)

# enemy event
ADDENEMY = pygame.USEREVENT + 1 
pygame.time.set_timer(ADDENEMY, enemySpawningSpeed)
ADDENEMYBULLET = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMYBULLET, enemyShootingSpeed)

player = Player()
enemies = pygame.sprite.Group()
enemybullets = pygame.sprite.Group()
playerbullets = pygame.sprite.Group()
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
        # spawn new enemy
        if event.type == ADDENEMY and len(enemies) < maxEnemyCount+1:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        # enemy fires
        if event.type == ADDENEMYBULLET:
            for enemy in enemies:
                for bullet in enemy.shoot():
                    enemybullets.add(bullet)
                    all_sprites.add(bullet)

    screen.blit(background, (0, 0))

    # player moves
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)  

    # player fires
    if pressed_keys[K_SPACE]:
        bullet = player.shoot()
        playerbullets.add(bullet)
        all_sprites.add(bullet)

    if pressed_keys[K_LSHIFT]:
        bullets = player.defense()
        for bullet in bullets:
            playerbullets.add(bullet)
            all_sprites.add(bullet)

    # update sprites
    enemies.update()
    enemybullets.update()
    playerbullets.update()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # check whether player collides with enemy's bullet
    playerHit = pygame.sprite.spritecollideany(player, enemybullets)
    if playerHit != None:
        playerHit.kill()
        if player.hp > 0:
            player.hp -= 1
        else:
            player.kill()
            running = False

    # check whether player's bullet hit anything
    for playerBullet in playerbullets:
        enemyHit = pygame.sprite.spritecollideany(playerBullet, enemies)
        bulletHit = pygame.sprite.spritecollideany(playerBullet, enemybullets)
        if enemyHit != None:
            if enemyHit.hp > 0:
                enemyHit.hp -= 1
            else:
                enemyHit.kill()
                playerBullet.kill()
        if bulletHit != None:
            bulletHit.kill()
            playerBullet.kill()

    pygame.display.update()
    clock.tick(FPS)
