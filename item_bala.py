import pygame, random
from constantes import *

# class Item_doble(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = pygame.image.load(r"items\bala_doble.png")
#         self.image = pygame.transform.scale(self.image, (30, 30))
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
#         self.rect.y = random.randrange(-100, -40)
#         self.speedy = random.randrange(1, 10)
#         self.speedx = random.randrange(-5, 5)

#     def update(self):
#         self.rect.x += self.speedx
#         self.rect.y += self.speedy

#         if self.rect.left < 0 or self.rect.right > ANCHO_PANTALLA:
#             self.speedx *= -1  # Invierte la dirección horizontal al chocar con los límites laterales

#         if self.rect.top < 0 or self.rect.bottom > ALTO_PANTALLA:
#             self.speedy *= -1  # Invierte la dirección vertical al chocar con los límites superior e inferior

class Item_doble(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.image.load(r"items\bala_doble.png")#.convert()
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