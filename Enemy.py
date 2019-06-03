"""The Enemy class"""

import pygame, random
from pygame.sprite import Sprite
from config import WHITE, WIDTH, HEIGHT, enemyImg, enemyHP, \
    enemyBulletImg
from Bullet import FourWayBullet

class Enemy(Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load(enemyImg).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(
            center=(random.randint(HEIGHT+50, HEIGHT+100), random.randint(0, WIDTH))
        )
        self.hp = enemyHP
        self.speed = random.randint(-10,10) 
        while self.speed == 0: self.speed = random.randint(-10,10) 

    def shoot(self):
        x = self.rect.centerx
        y = self.rect.centery
        bullets = []
        for i in range(4):
            bullets.append(FourWayBullet(x, y, i, enemyBulletImg))
        return bullets

    def update(self):
        self.rect.move_ip(self.speed, self.speed)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()
