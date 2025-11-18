import pygame
from paquete.funciones_especificas import *
from graficos.config import *
from paquete.calculos import *
pygame.init()

#Pantalla
rutas = ["Nonograma/archivos/auto.csv","Nonograma/archivos/buho.csv","Nonograma/archivos/cara_feliz.csv","Nonograma/archivos/gato.csv","Nonograma/archivos/inodoro.csv","Nonograma/archivos/hongo_malo.csv"]
ICONO = pygame.image.load("Nonograma/imagenes/icono_nonograma.png")
VENTANA = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
lista_coordendas_cruz = set()
lista_coordenadas_cuadrado = set()
coordenadas_suspendidas = set()
coordenadas_correctas = set()
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)
activo = True
contador = 0
reloj = pygame.time.Clock()
DELAY = 3000

tiempo_inicial = 0
tiempo_actual = 0
#POR HACER: CREAR UNA FUNCIÓN EN DONDE SE CALCULEN TODOS ESTOS DATOS. APORTANDO LEGIBILIDAD AL CÓDIGO.
datos = calcular_datos_nonograma(rutas)
dibujo_jugador = datos[0]
grilla_jugador = crear_matriz(len(dibujo_jugador), len(dibujo_jugador))

while activo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = evento.pos

            if validar_click_grilla(posicion_mouse):
                
                tiempo_inicial = pygame.time.get_ticks()
            #Porque saco la coordenda que no fué arreglada.
                if tiempo_actual == DELAY and chequear_casilla(dibujo_jugador,coordenadas_suspendidas[0]):
                    
                    coordenada_actual = coordenadas_suspendidas[0]
                    coordenadas_suspendidas.discard(coordenada_actual)
                    coordenadas_correctas.add(coordenada_actual)
                    tiempo_inicial = 0
                    tiempo_actual = 0

                if tiempo_actual == DELAY and chequear_casilla(dibujo_jugador,coordenadas_suspendidas[0]) == False:
                    
                    coordenada_actual = coordenadas_suspendidas[0]
                    
                    if dibujo_jugador[coordenada_actual[0]][coordenada_actual[1]] == 1:
                        lista_coordendas_cruz.add(coordenada_actual)
                        lista_coordenadas_cuadrado.discard(coordenada_actual)
                    else:
                        lista_coordenadas_cuadrado.add(coordenada_actual)
                        lista_coordendas_cruz.discard(coordenada_actual)
                    
                    coordenadas_correctas.add(coordenada_actual)
                
                if 0 < tiempo_actual < DELAY and evento.button == 1:
                    posicion_mouse = inicio_cuadrado(posicion_mouse,datos[5],(X_INICIO_GRILLA, Y_INICIO_GRILLA))
                    if posicion_mouse == coordenadas_suspendidas[0] and grilla_jugador[posicion_mouse[0]][posicion_mouse[1]] != 1:
                        lista_coordendas_cruz.add(posicion_mouse)
                        lista_coordenadas_cuadrado.discard(posicion_mouse)
        
                elif 0 < tiempo_actual < DELAY and evento.button == 3:
                    posicion_mouse = inicio_cuadrado(posicion_mouse,datos[5],(X_INICIO_GRILLA, Y_INICIO_GRILLA))
                    if posicion_mouse == coordenadas_suspendidas[0] and grilla_jugador[posicion_mouse[0]][posicion_mouse[1]] != 0:
                        lista_coordendas_cruz.discard(posicion_mouse)
                        lista_coordenadas_cuadrado.add(posicion_mouse)
                
                if evento.button == 1:
                        
                    #VISUAL
                    posicion_mouse = inicio_cuadrado(posicion_mouse,datos[5],(X_INICIO_GRILLA,Y_INICIO_GRILLA))
                    lista_coordenadas_cuadrado.add(posicion_mouse)

                    #LÓGICA
                    ubicacion_matriz = convertir_coordenadas(posicion_mouse,datos[1],datos[5], grilla_jugador)
                    pintar_casilla(grilla_jugador,ubicacion_matriz,1)            
                
                elif evento.button == 3:
                    pass
                coordenadas_suspendidas.add(posicion_mouse)

    VENTANA.fill(GRIS)

    pygame.draw.rect(VENTANA, 
                     BLANCO,
                     (X_INICIO_GRILLA, Y_INICIO_GRILLA, ANCHO_GRILLA, ALTO_GRILLA))
    
    dibujar_cuadrados_especificos(lista_coordenadas_cuadrado,datos[1],AZUL,VENTANA)

    #DIBUJA LINEAS
    funcion = dibujar("linea vertical")
    dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,VENTANA,funcion)

    funcion = dibujar("linea horizontal")
    dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,VENTANA,funcion,True)
    

    #DIBUJA LAS PISTAS
    mostrar_pistas_filas_pygame(datos[3],(X_INICIO_GRILLA -25,Y_INICIO_GRILLA),VENTANA,datos[2], NEGRO,datos[5])
    #DIBUJA LAS PISTAS DE LAS COLUMNAS.
    mostrar_pistas_columnas_pygame(datos[4],(X_INICIO_GRILLA, Y_INICIO_GRILLA - 25), VENTANA,datos[2],NEGRO,datos[5])
    
    tiempo_transcurrido = pygame.time.get_ticks()
    pygame.display.update()
pygame.quit()