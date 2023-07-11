import pygame
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400, 70))
pygame.display.set_caption('INGRESE SU NOMBRE')

lista =[]
fuente = pygame.font.Font(None, 32)
texto_ingresado = ""

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == K_BACKSPACE:
                texto_ingresado = texto_ingresado[:-1]
            elif event.key == K_RETURN:
                print("Texto ingresado:", texto_ingresado)
                texto_ingresado = ""
                lista.append(texto_ingresado)
            else:
                texto_ingresado += event.unicode
    ventana.fill((255, 255, 255))
    print(lista)
    texto_superficie = fuente.render(texto_ingresado, True, (0, 0, 0))
    ventana.blit(texto_superficie, (10, 10))
    pygame.display.update()
