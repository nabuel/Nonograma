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
grilla_jugador = crear_matriz(len(DIBUJO_CORRECTO), len(DIBUJO_CORRECTO),None)
grilla_coordenadas = cargar_coordenadas_grilla(grilla_jugador, longitud_celda,(X_INICIO_GRILLA,Y_INICIO_GRILLA))
lista_coordenadas_cruz = set()
lista_coordenadas_cuadrado = set()
coordenadas_correctas = set()
estado = None



dibujar_cuadrado = dibujar("cuadrado")
fila_columna_error_actual = None

#Configuración del reloj.
reloj = pygame.time.Clock()
DELAY = 3000  # 3 segundos de delay para celda incorrecta

tiempo_transcurrido = 0
tiempo_inicial = None
sin_tiempo = False




while activo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = pygame.mouse.get_pos()

            #Si la posición del mouse está dentro de la grilla.
            
            if validar_click_grilla(posicion_mouse):
                posicion_mouse = calcular_inicio_cuadrado(posicion_mouse, longitud_celda, (X_INICIO_GRILLA,Y_INICIO_GRILLA))
                valor_click = evento.button
                if valor_click == 1 or valor_click == 3:
                    estado = definir_estado_click(posicion_mouse, grilla_jugador, longitud_celda, valor_click, DIBUJO_CORRECTO,coordenadas_correctas)
                    
                    match estado:
                        case "correcto":
                            datos_click = manejar_click(valor_click, "correcto", coordenadas_correctas, lista_coordenadas_cruz, lista_coordenadas_cuadrado, posicion_mouse)
                            fila,columna = convertir_coordenadas_matriz(posicion_mouse, (X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)
                            
                            if valor_click == 1:
                                grilla_jugador[fila][columna] = 1
                            elif valor_click == 3:
                                grilla_jugador[fila][columna] = 0
                            
                            tiempo_inicial = 0
                            tiempo_transcurrido = 0
                            if fila_columna_error_actual != None:
                                fila,columna = fila_columna_error_actual

                            
                        case "incorrecto":
                            datos_click = manejar_click(valor_click, "incorrecto", coordenadas_correctas, lista_coordenadas_cruz, lista_coordenadas_cuadrado,posicion_mouse)
                            
                            print(lista_coordenadas_cruz)
                            print(lista_coordenadas_cuadrado)
                            
                            fila, columna = convertir_coordenadas_matriz(posicion_mouse, (X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)
                            grilla_jugador = pintar_casilla(grilla_jugador, (fila,columna),invertir_cuadrado(valor_click))
                            if posicion_mouse not in coordenadas_correctas:
                                vidas -= 1
                                grilla_jugador = pintar_casilla(grilla_jugador, (fila,columna),invertir_cuadrado(valor_click))
                                lista_coordenadas_cruz, lista_coordenadas_cuadrado = arreglar_coordenadas_pygame(valor_click, posicion_mouse,lista_coordenadas_cruz,lista_coordenadas_cuadrado)
                                print(f"Casilla incorrecta. Pierdes una vida. Vidas restantes: {vidas}")
                            print("-------------------------------")
                            print(lista_coordenadas_cruz)
                            print(lista_coordenadas_cuadrado)
                            
                            print(f"No se puede marcar una casillas ")

                        case _:
                            pass
                            
                    
        if chequear_dibujo_terminado(grilla_jugador, DIBUJO_CORRECTO):
            print("¡Felicidades! Has completado el nonograma.")
            activo = False
        
    VENTANA.fill(GRIS)

    
    if vidas == 0:
        print("Juego terminado. No te quedan vidas.")
        activo = False
    
    
    dibujar_cuadrado((ANCHO_GRILLA, ALTO_GRILLA), (X_INICIO_GRILLA, Y_INICIO_GRILLA), BLANCO, VENTANA)
    
    
    mostrar_pistas_filas_pygame(datos[3],(X_INICIO_GRILLA -25,Y_INICIO_GRILLA),VENTANA,datos[2], NEGRO,datos[5])
    #DIBUJA LAS PISTAS DE LAS COLUMNAS.
    mostrar_pistas_columnas_pygame(datos[4],(X_INICIO_GRILLA, Y_INICIO_GRILLA - 25), VENTANA,datos[2],NEGRO,datos[5])

    
    if len(lista_coordenadas_cuadrado) > 0:
        dibujar_cuadrados_especificos(lista_coordenadas_cuadrado, datos[1], AZUL, VENTANA)
    
    if len(lista_coordenadas_cruz) > 0:
        dibujar_cruces_especificas(lista_coordenadas_cruz, datos[5], ROJO, VENTANA)
    
    #DIBUJA LINEAS
    funcion = dibujar("linea vertical")
    dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,VENTANA,funcion)

    funcion = dibujar("linea horizontal")
    dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,VENTANA,funcion,True)
    

    
    pygame.display.update()

pygame.quit()