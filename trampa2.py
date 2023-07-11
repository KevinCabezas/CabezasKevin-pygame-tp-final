import pygame, random
from constantes import*

class Asteroide(pygame.sprite.Sprite):
	def __init__(self):	
		super().__init__()
		self.image = pygame.image.load(r"recursos1\asteroide.png").convert()
		numero_random = random.randint(20,120)
		self.image = pygame.transform.scale(self.image,(numero_random,numero_random))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		# self.rect.x = 5
		# self.rect.y = 5
		self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speedy = random.randrange(1, 10)

		# self.grupo = grupo_sprites

	def update(self):
		# self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > ALTO_PANTALLA + 10 or self.rect.left < -25 or self.rect.right > ANCHO_PANTALLA + 22 :
			self.rect.x = random.randrange(ANCHO_PANTALLA - self.rect.width)
			self.rect.y = random.randrange(-100, -40)
			self.speedy = random.randrange(1, 10)
			# if self.grupo != None:
			# 	self.grupo.remove(self)