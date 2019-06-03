"""The Bullet class"""

import pygame
from pygame.sprite import Sprite
from config import WIDTH, HEIGHT, WHITE, playerBulletSpeed, \
    defenseDistance, enemyBulletSpeed

class OneWayBullet(Sprite):
    def __init__(self, x, y, img):
        super(OneWayBullet, self).__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = playerBulletSpeed

    def update(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()


class FourWayBullet(Sprite):
    def __init__(self, x, y, d, img):
        super(FourWayBullet, self).__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedx = 0
        self.speedy = 0
        if d == 0:
            self.speedx = enemyBulletSpeed
        elif d == 1:
            self.speedy = enemyBulletSpeed
        elif d == 2:
            self.speedx = -enemyBulletSpeed
        elif d == 3:
            self.speedy= -enemyBulletSpeed

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()


class EightWayBullet(Sprite):
    def __init__(self, x, y, d, img):
        super(EightWayBullet, self).__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedx = 0
        self.speedy = 0
        self.orgx = x
        self.orgy = y
        if d == 0 or d == 4 or d == 7:
            self.speedy = -playerBulletSpeed
        if d == 1 or d == 4 or d == 5:
            self.speedx = playerBulletSpeed
        if d == 2 or d == 5 or d == 6:
            self.speedy = playerBulletSpeed
        if d == 3 or d == 6 or d == 7:
            self.speedx = -playerBulletSpeed

    def update(self):
        vx = self.speedx
        vy = self.speedy
        if self.speedx != 0 and self.speedy != 0:
            vx = vx*0.707
            vy = vy*0.707
        self.rect.move_ip(vx, vy)
        x = self.rect.centerx - self.orgx
        y = self.rect.centery - self.orgy
        if (x*x + y*y) > (defenseDistance * defenseDistance):
            self.kill()
