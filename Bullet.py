"""The Bullet class"""

import pygame
from pygame.sprite import Sprite
from config import WIDTH, HEIGHT, WHITE

class BulletBase(Sprite):
    def __init__(self, img, x, y, speedx, speedy):
        super(BulletBase, self).__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.speedx = speedx
        self.speedy = speedy

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
            self.rect.centery < 0 or self.rect.centery > HEIGHT:
            self.kill()


class BulletFixed(BulletBase):
    def __init__(self, img, x, y, speed, mode, distance):
        super(BulletFixed, self).__init__(img, x, y, 0, 0)
        self.orgX = x
        self.orgY = y
        self.maxD = distance
        if mode == 0 or mode == 4 or mode == 7:
            self.speedy = -speed
        if mode == 1 or mode == 4 or mode == 5:
            self.speedx = speed
        if mode == 2 or mode == 5 or mode == 6:
            self.speedy = speed
        if mode == 3 or mode == 6 or mode == 7:
            self.speedx = -speed

    def update(self):
        vx = self.speedx
        vy = self.speedy
        if (self.speedx != 0) and (self.speedy != 0):
            vx = vx*0.707
            vy = vy*0.707        
        self.rect.move_ip(vx, vy)
        x = self.rect.centerx - self.orgX
        y = self.rect.centery - self.orgY
        if self.maxD == 0:
            if self.rect.centerx < 0 or self.rect.centerx > WIDTH or \
                self.rect.centery < 0 or self.rect.centery > HEIGHT:
                self.kill()
        else: 
            if (x*x + y*y) > (self.maxD * self.maxD):
                self.kill()    
