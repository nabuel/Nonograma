import time
import pygame
from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *


pygame.init()
activo = True


#Configuración pantalla
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
ICONO = pygame.image.load("Nonograma/imagenes/icono_nonograma.png")
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)


#Configuración nonograma.
rutas = ["Nonograma/archivos/auto.csv","Nonograma/archivos/buho.csv","Nonograma/archivos/cara_feliz.csv","Nonograma/archivos/gato.csv","Nonograma/archivos/inodoro.csv","Nonograma/archivos/hongo_malo.csv"]
datos = calcular_datos_nonograma(rutas)
DIBUJO_CORRECTO = datos[0]
longitud_celda = datos[5]
vidas = 3

#Ordenamiento de datos.
grilla_jugador = crear_matriz(len(DIBUJO_CORRECTO), len(DIBUJO_CORRECTO))
lista_coordenadas_cruz = set()
lista_coordenadas_cuadrado = set()
coordenadas_suspendidas = []
coordenadas_correctas = set()
contador = 0
posicion_mouse_suspendida = None


#Configuración del reloj.
reloj = pygame.time.Clock()
# DELAY = 3000
# SIN_TIEMPO = pygame.USEREVENT + 1
# pygame.time.set_timer(SIN_TIEMPO, 0)
# tiempo_inicial = 0



while activo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False

        
    pygame.display.update()

pygame.quit()