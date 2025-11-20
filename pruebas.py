from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *
from paquete.validaciones import * 
import pygame

pygame.init()
pygame.font.init()

rutas = ["Nonograma/archivos/auto.csv","Nonograma/archivos/buho.csv","Nonograma/archivos/cara_feliz.csv","Nonograma/archivos/gato.csv","Nonograma/archivos/inodoro.csv","Nonograma/archivos/hongo_malo.csv"]
datos = calcular_datos_nonograma(rutas)
DIBUJO_CORRECTO = datos[0]
grilla_jugador = crear_matriz(len(DIBUJO_CORRECTO), len(DIBUJO_CORRECTO))
longitud_celda = datos[5]

matriz_logica = cargar_coordenadas_grilla(grilla_jugador,longitud_celda,(X_INICIO_GRILLA,Y_INICIO_GRILLA))

mostrar_matriz(matriz_logica)