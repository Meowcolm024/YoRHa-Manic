"""The Player class"""

import pygame
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from config import WHITE, WIDTH, HEIGHT, saberImg, playerSpeed, \
    playerHP, playerBulletImg, playerBulletSpeed


class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(saberImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.hp = playerHP

    def shoot(self):
        bullet = PlayerBullets(self.rect.centerx, self.rect.centery)
        return bullet

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-playerSpeed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,playerSpeed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-playerSpeed,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(playerSpeed,0)
        # check if the player is out of border
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.centery < 0:
            self.rect.centery = 0


class PlayerBullets(Sprite):
    def __init__(self, x, y):
        super(PlayerBullets, self).__init__()
        self.image = pygame.image.load(playerBulletImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = playerBulletSpeed

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()