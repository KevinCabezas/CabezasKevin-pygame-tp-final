import pygame,random
from constantes import*
from balas_enemigo import Bullet

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,grupo_sprites,bullets):
        super().__init__()
        self.grupo_sprites = grupo_sprites
        self.bullets = bullets
        self.imagen = pygame.image.load(r"recursos\nave_enemiga2.png")#.convert()
        # self.imagen.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.imagen,(97,75))
        self.rect = self.image.get_rect()
        self.rect.centerx =  -150
        self.rect.bottom = + 120
        self.speed_x = 2
        self.vida = 200
        self.tiempo_disparo = 0  # Variable para controlar el tiempo entre disparos
        self.frecuencia_disparo = 400  # Tiempo en milisegundos entre cada disparo
        # self.shield = 100
    def update(self):
        if self.vida <= 0:
            self.kill()#borrar eneimgo de los grupos
            self.rect = pygame.Rect(0,0,0,0)
        else:
            self.rect.x += self.speed_x
            # Controlar los límites de la pantalla
            if self.rect.right > ANCHO_PANTALLA:
                self.speed_x = -2  # Cambiar dirección al llegar al borde derecho
            if self.rect.left < 0:
                self.speed_x = 2  # Cambiar dirección al llegar al borde izquierdo
        # Controlar la frecuencia de disparo
        tiempo_actual = pygame.time.get_ticks()  # Obtener el tiempo actual en milisegundos
        if tiempo_actual - self.tiempo_disparo >= self.frecuencia_disparo:
            self.shooot()  # Realizar el disparo
            self.tiempo_disparo = tiempo_actual  # Actualizar el tiempo de último disparo
    
    def shooot(self):
        balas = Bullet(self.rect.centerx, self.rect.top,"recursos\laser.gren.png")
        self.grupo_sprites.add(balas)
        self.bullets.add(balas)