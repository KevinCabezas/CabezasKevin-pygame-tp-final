import pygame,random
from constantes import *

class Item_fuego(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(r"items/bala_fuego.png")#.convert()
		# self.image.set_colorkey(WHITE)
		self.image = pygame.transform.scale(self.image,(30,30))
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)
		self.speedx = random.randrange(-5, 5)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > ALTO_PANTALLA + 10 or self.rect.left < -25 or self.rect.right > ANCHO_PANTALLA + 22 :
			self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 8)