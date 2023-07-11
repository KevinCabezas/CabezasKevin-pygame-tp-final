import pygame
import sys
from constantes import*
from player import Player
from trampas import Meteoro
from trampa2 import Asteroide
from explocion import Explosion
from vida import Vida
pygame.init()
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
grupo_sprites = pygame.sprite.Group()#cramos un grupo de sprites
lista_meteoros = pygame.sprite.Group() 
lista_asteroide = pygame.sprite.Group()
bullets = pygame.sprite.Group()
vida = Vida()
player = Player()
grupo_sprites.add(player) #agregamos los sprites del player al grupo

# for i in range(8):
# 	meteor = Meteoro()
# 	grupo_sprites.add(meteor)
# 	lista_meteoros.add(meteor)
vida.vida_player()
        
for i in range(8):
    asteriode = Asteroide()
    grupo_sprites.add(asteriode)
    lista_asteroide.add(asteriode)
reloj = pygame.time.Clock()
imagen_fondo = pygame.image.load(r"C:\Users\Usuario\OneDrive\Escritorio\copia _juego nave\recursos1\espacio.png").convert()

imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                player.shoot()

    # Renderizado de la pantalla
    pantalla.blit(imagen_fondo,(0,0))
 
    #dibujar vidas  
    # Lógica del juego
    grupo_sprites.update()
    # for sprite in grupo_sprites: # Dibujar sprites en la pantalla
    #     sprite.draw(pantalla)

    # Colisiones meteoro - laser
    hits = pygame.sprite.groupcollide(lista_asteroide,bullets,True,True)
    for hit in hits:  
        explocion = Explosion(hit.rect.center)
        grupo_sprites.add(explocion)

        asteriode = Asteroide()    
        grupo_sprites.add(asteriode)
        lista_asteroide.add(asteriode)
		
	# Colisiones jugador - meteoro
    # vida.colicion_jugador_trampa(player,lista_asteroide,False)
    hits = pygame.sprite.spritecollide(player, lista_asteroide, True)
    for hit in hits:
        player.shield -=25
        asteriode = Asteroide()    
        grupo_sprites.add(asteriode)
        lista_asteroide.add(asteriode)
        # print("daño")
        
        daño = True
        vida.eliminar_vidas(daño)
    orden = vida.vidas_nada 
    running = orden
    grupo_sprites.draw(pantalla)
    # Dibujar elementos en la pantalla
    vida.dibujar_vidas(pantalla)
    pygame.display.flip()
    reloj.tick(60)
