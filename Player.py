"""The Player class"""

import pygame
from pygame.sprite import Sprite
from config import whiteColor, saberImg


class Player(Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load(saberImg)#.convert()
        self.image.set_colorkey(whiteColor)
        self.rect = self.image.get_rect()
