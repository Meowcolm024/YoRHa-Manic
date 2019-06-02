"""The Enemy class"""

import pygame, random
from pygame.sprite import Sprite
from config import WHITE, WIDTH, HEIGHT, enemyImg, enemyBulletImg, enemyBulletSpeed

class Enemy(Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(enemyImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(
            center=(random.randint(HEIGHT+50, HEIGHT+100), random.randint(0, WIDTH))
        )
        self.speed = random.randint(-10,10) 
        while self.speed == 0: self.speed = random.randint(-10,10) 

    def shoot(self):
        x = self.rect.centerx
        y = self.rect.centery
        bullets =[]
        for i in range(4):
            bullets.append(EnemyBullets(x, y, i))
        return bullets

    def update(self):
        self.rect.move_ip(self.speed, self.speed)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()


class EnemyBullets(Sprite):
    def __init__(self, x, y, d):
        super(EnemyBullets, self).__init__()
        self.image = pygame.image.load(enemyBulletImg).convert_alpha()
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
