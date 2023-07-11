import pygame
from constantes import*
# pygame.init
class Vida():
    def __init__(self) -> None:
        self.lista_vidas = []
        self.vidas_nada = True
        self.imagen_d = pygame.image.load(r"items\bala_doble.png")
        self.imagen_d = pygame.transform.scale(self.imagen_d,(20,20)) 
        self.imagen_f = pygame.image.load(r"items\bala_fuego.png")
        self.imagen_f = pygame.transform.scale(self.imagen_f,(20,20))  
        self.item_a_mostrar = False
    def vida_player(self):
        for indice in range(5):
            self.vida_sprite = pygame.image.load("recursos\corazon.png")
            self.vida = pygame.transform.scale(self.vida_sprite,(27,20))
            self.lista_vidas.append(self.vida)
            # print("hola")
        # print(lista_vidas)
        # return lista_vidas
    def dibujar_vidas(self,superficie,tipo_item):
        x = 10
        y = 20
        # lista_vidas = vida_player()
        for imagen in self.lista_vidas:
            rect_imagen = imagen.get_rect()
            rect_imagen.topleft = (x, y)
            # superficie.blit(imagen, rect_imagen)
            x += rect_imagen.width + 5  # Ajusta la posición en X para la siguiente imagen
            superficie.blit(imagen,rect_imagen)
        if tipo_item == "D":
            x = 20
            y = 60
            rect_imagen = self.imagen_d.get_rect()
            rect_imagen.topleft = (x, y)
            superficie.blit(self.imagen_d,rect_imagen)
    def eliminar_vidas(self,choque):
            if choque:
                if len(self.lista_vidas) > 0:
                # Eliminar una imagen de vidas
                    self.lista_vidas.pop()
                    if len(self.lista_vidas) == 0 :
                        self.vidas_nada = False
                        # print("menos")
    def aumentar_vida(self,choque):
        if choque and len(self.lista_vidas) <= 7:
            self.lista_vidas.append(self.vida)

  