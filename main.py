import pygame
from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *


pygame.init()
activo = True


#Configuración pantalla
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
FONDO_IMAGEN = pygame.image.load("Nonograma/imagenes/fondo_nonograma.png")
VENTANA.blit(FONDO_IMAGEN, (0, 0))
ICONO = pygame.image.load("Nonograma/imagenes/icono_nonograma.png")
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)


estado = ""

while activo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            if evento.button == 1:  # Click izquierdo
                # nombre = obtener_nombre_boton(VENTANA, posicion_mouse)
                estado = jugar_nonograma_pygame(VENTANA, ICONO, FONDO_IMAGEN)
                vidas, tiempo = estado
                if vidas > 0:

                    actualizar_ranking()
                    puntuacion = calcular_puntuacion(tiempo, vidas)
                    
                    escribir_csv(ranking,)
                    ranking = convertir_csv_matriz("Nonograma/archivos/ranking.csv")
                    ordenar_ranking(ranking)
            print(puntuacion)
            

    
    pygame.display.update()

pygame.quit()