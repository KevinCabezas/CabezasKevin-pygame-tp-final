import pygame
from pygame.locals import *

class Mira(pygame.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

pygame.init()
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
FPS = 60

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
reloj = pygame.time.Clock()

mira = Mira("recursos\mira.png")
grupo_sprites = pygame.sprite.Group()
grupo_sprites.add(mira)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    grupo_sprites.update()

    pantalla.fill((255, 255, 255))
    grupo_sprites.draw(pantalla)

    pygame.display.flip()
    reloj.tick(FPS)
