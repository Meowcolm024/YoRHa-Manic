"""The Player class"""

import pygame
from pygame.sprite import Sprite
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
from config import whiteColor, saberImg, playerSpeed


class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(saberImg).convert_alpha()
        self.image.set_colorkey(whiteColor)
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-playerSpeed)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,playerSpeed)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-playerSpeed,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(playerSpeed,0)
