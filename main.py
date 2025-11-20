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
grilla_coordenadas = cargar_coordenadas_grilla(grilla_jugador, longitud_celda, (X_INICIO_GRILLA,Y_INICIO_GRILLA))
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
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()
            posicion_mouse = calcular_inicio_cuadrado(posicion_mouse, longitud_celda, (X_INICIO_GRILLA,Y_INICIO_GRILLA))
            valor_click = evento.button
            #Si la posición del mouse está dentro de la grilla. 
            if posicion_mouse in grilla_coordenadas:
                if valor_click == 1 or valor_click == 3:
                    match definir_estado_click(posicion_mouse, grilla_jugador, longitud_celda, valor_click):
                        case "correcto":
                            datos_click = manejar_click(valor_click, "correcto", coordenadas_correctas, coordenadas_suspendidas, lista_coordenadas_cruz, lista_coordenadas_cuadrado)
                            coordenadas_correctas = datos_click[0]
                        case "incorrecto":
                            #Acá inicia el contador de 3 segundos.
                            datos_click = manejar_click(valor_click, "incorrecto", coordenadas_correctas, coordenadas_suspendidas, lista_coordenadas_cruz, lista_coordenadas_cuadrado)
                            coordenadas_suspendidas = datos_click[1]
                            posicion_mouse_suspendida = coordenadas_suspendidas[0]
                            lista_coordenadas_cuadrado = datos_click[3]

                        case "revertir":
                            manejar_click(valor_click, "revertir", coordenadas_correctas, coordenadas_suspendidas, lista_coordenadas_cruz, lista_coordenadas_cuadrado)
                            
                            coordenadas_correctas = datos_click[0]
                            lista_coordenadas_cruz = datos_click[2]
                            lista_coordenadas_cuadrado = datos_click[3]
    
            

        
    pygame.display.update()

pygame.quit()