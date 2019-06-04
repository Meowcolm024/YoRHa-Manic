"""The Enemy class"""

import pygame, random
from pygame.sprite import Sprite
from config import WHITE, WIDTH, HEIGHT, enemyImg, enemyHP, \
    enemyBulletImg, enemyBulletSpeed
from Bullet import BulletFixed

class Enemy(Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(enemyImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(
            center=(random.randint(HEIGHT+50, HEIGHT+100), random.randint(0, WIDTH))
        )
        self.hp = enemyHP
        self.speedx = random.randint(-10,10) 
        self.speedy = random.randint(-10,10)
        while self.speedx == 0: self.speedx = random.randint(-10,10) 
        while self.speedy == 0: self.speedy = random.randint(-10,10) 

    def shoot(self):
        x = self.rect.centerx
        y = self.rect.centery
        bullets = []
        for i in range(4):
            bullets.append(
                BulletFixed(enemyBulletImg, x, y, enemyBulletSpeed, i, 0)
                )
        return bullets

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH :
            self.speedx = -self.speedx
        if self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.speedy = -self.speedy
