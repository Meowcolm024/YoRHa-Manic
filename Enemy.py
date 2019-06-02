"""The Enemy class"""

import pygame, random
from pygame.sprite import Sprite
from config import WHITE, WIDTH, HEIGHT, emenyImg

class Enemy(Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(emenyImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(
            center=(random.randint(HEIGHT+50, HEIGHT+100), random.randint(0, WIDTH))
        )
        self.speed = random.randint(5,10)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.centerx < 0:
            self.kill()