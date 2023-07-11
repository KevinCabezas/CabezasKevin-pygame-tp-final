import pygame, random
from constantes import *

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("recursos1\laser1.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y - 27
        self.rect.centerx = x + 1
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

    # def fire_bullet(self, bullet_group):
    #     bullet1 = Bullets(self.rect.centerx - 10, self.rect.y)
    #     bullet2 = Bullets(self.rect.centerx + 10, self.rect.y)
    #     bullet_group.add(bullet1, bullet2)
