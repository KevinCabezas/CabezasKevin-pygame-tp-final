import pygame,sys,random
from auxiliar import*
# from pygame.sprite import _Group
from constantes import*
from explocion import Explosion
# from pygame.locals import *
class Bomba(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos1\meteorGrey_tiny1.png")
        self.rect = self.image.get_rect()
        self.velocidad = 2

        # Establecer la posición inicial en los laterales, arriba o abajo
        self.posicion_inicial()

    def posicion_inicial(self):
        lado = random.choice(["izquierda", "derecha", "arriba", "abajo"])

        if lado == "izquierda":
            self.rect.left = 0
            self.rect.centery = random.randint(0, ALTO_PANTALLA)
        elif lado == "derecha":
            self.rect.right = ANCHO_PANTALLA
            self.rect.centery = random.randint(0, ALTO_PANTALLA)
        elif lado == "arriba":
            self.rect.top = 0
            self.rect.centerx = random.randint(0, ANCHO_PANTALLA)
        elif lado == "abajo":
            self.rect.bottom = ALTO_PANTALLA
            self.rect.centerx = random.randint(0, ANCHO_PANTALLA)

    def update(self):
        objetivo_x = ANCHO_PANTALLA // 2
        objetivo_y = ALTO_PANTALLA // 2

        dx = objetivo_x - self.rect.centerx
        dy = objetivo_y - self.rect.centery -50

        distancia = abs(dx) + abs(dy)
        velocidad_x = dx / distancia * self.velocidad
        velocidad_y = dy / distancia * self.velocidad

        self.rect.x += velocidad_x
        self.rect.y += velocidad_y
class Planeta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"recursos\tierra.png")
        self.image = pygame.transform.scale(self.image,(90,90))
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2 - 50)
class Mira(pygame.sprite.Sprite):
    def __init__(self, ) -> None:
        super().__init__()
        self.image = pygame.image.load("recursos\mira.png")
        # imagen.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (ANCHO_PANTALLA / 2,ALTO_PANTALLA - 110)

    def update(self):
        # Actualizar la posición del sprite según la posición del mouse
        self.rect.center = pygame.mouse.get_pos()
class Punto(pygame.sprite.Sprite):
    def __init__(self, ) -> None:
        super().__init__()
        self.image = pygame.image.load("recursos\proyectil.png")
        # imagen.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image,(6,3))
        self.rect = self.image.get_rect()
        self.rect.topleft = (ANCHO_PANTALLA / 2,ALTO_PANTALLA - 110)

    def update(self):
        # Actualizar la posición del sprite según la posición del mouse
        self.rect.center = pygame.mouse.get_pos()       
pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
reloj = pygame.time.Clock()
grupo_sprite = pygame.sprite.Group()
grupo_bombas = pygame.sprite.Group()
# mira = pygame.sprite.Group()
tierra = Planeta()
grupo_sprite.add(tierra)

mira = Mira()
grupo_sprite.add(mira)
punto = Punto()
grupo_sprite.add(punto)
# colicion mira bomba
for _ in range(10):
    bomba = Bomba()
    grupo_bombas.add(bomba)
    grupo_sprite.add(bomba)
def colicion_mira_bomba():
    impactos = pygame.sprite.spritecollide(punto,grupo_bombas,True)
    for impacto in impactos:
        punto_explocion = (impacto.rect.center)
        explocion = Explosion(punto_explocion)
        grupo_sprite.add(explocion)
        grupo_sprite.add(explocion)
        bomba = Bomba()
        grupo_bombas.add(bomba)
        grupo_sprite.add(bomba)
        play_soud("sonido\BANGMED.WAV")
    play_soud("recursos1\laser5.ogg")

def colision_bomba_tierra():
    hits = pygame.sprite.spritecollide(tierra,grupo_bombas, True)
    for hit in hits:
        punto_explocion = (hit.rect.center[0]+20,hit.rect.center[1]-20)

        explocion = Explosion(punto_explocion)
        grupo_sprite.add(explocion)
        bomba = Bomba()
        grupo_bombas.add(bomba)
        grupo_sprite.add(bomba) 
    
def play_soud(ruta):
        sonido_disparo = pygame.mixer.Sound(ruta)
        sonido_disparo.play()
        volumen = VOLUMEN
        sonido_disparo.set_volume(volumen)
imagen_fondo = pygame.image.load(r"C:\Users\Usuario\OneDrive\Escritorio\copia _juego nave\recursos1\espacio.png").convert()
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.mouse.set_visible(False)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN :
            colicion_mira_bomba()
            print("disparo")
    pantalla.blit(imagen_fondo,(0,0))
    grupo_sprite.update()
   
    grupo_sprite.draw(pantalla)
    colision_bomba_tierra()
    dibujar_sprite_estatico(r"panel\barra.png",pantalla,0,ALTO_PANTALLA - 200,1202,200)
    dibujar_sprite_estatico("panel\panel1.png",pantalla,150,ALTO_PANTALLA - 105,160,100)
    dibujar_sprite_estatico("panel\panel2.png",pantalla,350,ALTO_PANTALLA - 105,200,105)
    dibujar_sprite_estatico("panel\panel3.png",pantalla,600,ALTO_PANTALLA - 105,200,105)
    dibujar_sprite_estatico("panel\panel4.png",pantalla,840,ALTO_PANTALLA - 105,200,100)


    pygame.display.flip()
    reloj.tick(FPS)
