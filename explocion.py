import pygame
from constantes import*

def cargar_imagenes():
	
    explosion_anim = []
    for indice in range(9):
        file = r"recursos1\regularExplosion0{0}.png".format(indice)
        img = pygame.image.load(file).convert()
        img.set_colorkey(BLACK)
        img_scale = pygame.transform.scale(img, (50, 50))#origen 70
        explosion_anim.append(img_scale)
    return explosion_anim
class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.lista_explocion = cargar_imagenes()
		self.image = self.lista_explocion[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 # how long to wait for the next frame VELOCITY OF THE EXPLOSION

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(self.lista_explocion):
				self.kill() # if we get to the end of the animation we don't keep going.
			else:
				center = self.rect.center
				self.image = self.lista_explocion[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center