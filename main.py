import pygame
from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *
from paquete.estado_juego import *


pygame.init()
activo = True


#Configuración pantalla
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
FONDO_IMAGEN = pygame.image.load("imagenes/fondo_nonograma.png")
VENTANA.blit(FONDO_IMAGEN, (0, 0))
ICONO = pygame.image.load("imagenes/icono_nonograma.png")
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)

#Configuración de estados.
MENU = 1
JUEGO = 2
RANKING = 3

nombre_jugador = ""
ejecutar = MENU

while activo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
        
        if ejecutar == MENU:
            ejecutar = mostrar_menu(VENTANA, FONDO_IMAGEN)
        elif ejecutar == JUEGO:
            estado = jugar_nonograma_pygame(VENTANA,FONDO_IMAGEN)
            vidas, tiempo, nombre = estado
            ejecutar = 1
            if vidas > 0:
                actualizar_ranking(tiempo,vidas,nombre)
        elif ejecutar == RANKING:
            mostrar_ranking("archivos/ranking.csv",10)
            ejecutar = 1
            

    
    pygame.display.update()

pygame.quit()