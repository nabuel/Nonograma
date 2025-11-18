import pygame
from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *
pygame.init()

#Pantalla
rutas = ["Nonograma/archivos/auto.csv","Nonograma/archivos/buho.csv","Nonograma/archivos/cara_feliz.csv","Nonograma/archivos/gato.csv","Nonograma/archivos/inodoro.csv","Nonograma/archivos/hongo_malo.csv"]
ICONO = pygame.image.load("Nonograma/imagenes/icono_nonograma.png")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
lista_coordenadas = []
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)
activo = True
contador = 0

#POR HACER: CREAR UNA FUNCIÓN EN DONDE SE CALCULEN TODOS ESTOS DATOS. APORTANDO LEGIBILIDAD AL CÓDIGO.
datos = calcular_datos_nonograma(rutas)

while activo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = evento.pos
            if evento.button == 1:
                posicion_mouse = inicio_cuadrado(posicion_mouse,datos[5],(X_INICIO,Y_INICIO))
                lista_coordenadas.append(posicion_mouse)
                dibujar_cuadrados_especificos(lista_coordenadas,datos[1],AZUL,VENTANA)
                # pintar_casilla


    VENTANA.fill(GRIS)

    pygame.draw.rect(VENTANA, 
                     BLANCO,
                     (X_INICIO, Y_INICIO, ANCHO_CUADRADO, ALTO_CUADRADO))
    
    dibujar_cuadrados_especificos(lista_coordenadas,datos[1],AZUL,VENTANA)

    #DIBUJA LINEAS
    funcion = dibujar("linea vertical")
    dibujar_lineas((X_INICIO,Y_INICIO), datos[5],len(datos[0]),NEGRO,VENTANA,funcion)

    funcion = dibujar("linea horizontal")
    dibujar_lineas((X_INICIO,Y_INICIO), datos[5],len(datos[0]),NEGRO,VENTANA,funcion,True)
    

   

    #DIBUJA LAS PISTAS
    mostrar_pistas_filas_pygame(datos[3],(X_INICIO -25,Y_INICIO),VENTANA,datos[2], NEGRO,datos[5])
    #DIBUJA LAS PISTAS DE LAS COLUMNAS.
    mostrar_pistas_columnas_pygame(datos[4],(X_INICIO, Y_INICIO - 25), VENTANA,datos[2],NEGRO,datos[5])
    
    
    pygame.display.update()
pygame.quit()