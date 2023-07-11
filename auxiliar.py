import pygame
from constantes import*



def dibujar_sprite_estatico(ruta,superficie,pos_x,pos_y,x,y):
    imagen = pygame.image.load(ruta) 
    imagen = pygame.transform.scale(imagen,(x,y))
    rect_imagen = imagen.get_rect()
    rect_imagen.topleft = (pos_x, pos_y)  # Establecer las coordenadas de ubicación
    superficie.blit(imagen,rect_imagen)

def dibujar_texto(texto, color, superficie, pos_x, pos_y,tamaño):
    fuente_texto = r"C:\Windows\Fonts\AGENCYB.TTF"
    fuente = pygame.font.Font(fuente_texto, tamaño)
    texto_renderizado = fuente.render(texto, True, color)
    rect_texto = texto_renderizado.get_rect()
    rect_texto.topleft = (pos_x, pos_y)
    superficie.blit(texto_renderizado, rect_texto)

def play_soud(ruta,volumen):
        # pygame.mixer.init()
        sonido = pygame.mixer.Sound(ruta)
        sonido.set_volume(volumen)
        sonido.play()

class Boton(pygame.sprite.Sprite):
    def __init__(self, imagen, x, y,size=None):
        super().__init__()
        self.image = pygame.image.load(imagen).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)