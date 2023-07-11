import pygame,sys
from constantes import*
from trampas import Meteoro
from trampa2 import Asteroide
from explocion import Explosion
from vida import Vida
from player import Player
from items import Item
from enemigo import Enemigo
from balas import Bullet
from item_bala import Item_doble
from item_fuego import Item_fuego


class Logica():
    def __init__(self,pantalla) -> None:
        pygame.init()
        self.grupo_sprites = pygame.sprite.Group()
        self.lista_meteoros = pygame.sprite.Group()
        self.lista_asteroide = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.grupo_items_vida = pygame.sprite.Group()
        self.grupo_items_doble = pygame.sprite.Group()
        self.grupo_items_fuego = pygame.sprite.Group()
        self.pantalla = pantalla
        # self.grupo_bullet_doble = pygame.sprite.Group()

        self.vida = Vida()

        self.player = Player(self.grupo_sprites,self.bullets)
        self.grupo_sprites.add(self.player)
        self.enemigo = Enemigo()
        # self.grupo_sprites.add(self.enemigo)

        self.vida.vida_player()
        self.cambiar_bala_doble = False
        self.cambiar_bala_fuego = False
        self.cambiar_bala_simple = True

        self.fps = FPS
        self.paused = False
        self.mostrar_texto = False
        self.tiempo_inicial = 0
        self.tiempo_mostrando_texto = 600  # 3000 milisegundos (3 segundos)
        for i in range(0):
            asteriode = Asteroide()
            self.grupo_sprites.add(asteriode)
            self.lista_asteroide.add(asteriode)
        # lista_items = []
        for i in range(1):
            item = Item()
            self.grupo_sprites.add(item) 
            self.grupo_items_vida.add(item)
            # self.grupo_sprites.add(item)
            # lista_items.append(item)
        for i in range(1):
            item_doble_bala = Item_doble()
            self.grupo_sprites.add(item_doble_bala)
            self.grupo_items_doble.add(item_doble_bala)
        for i in range(1):
            item_fuego = Item_fuego()
            self.grupo_sprites.add(item_fuego)
            self.grupo_items_fuego.add(item_fuego)
    def colicion_item_vida_player(self):
        choques = pygame.sprite.spritecollide(self.player,self.grupo_items_vida,True)
        for choque in choques:
            item_vida = Item()
            self.grupo_sprites.add(item_vida)
            self.grupo_items_vida.add(item_vida)   
            self.vida.aumentar_vida(True)
        self.grupo_sprites.draw(self.pantalla)
        self.vida.dibujar_vidas(self.pantalla)