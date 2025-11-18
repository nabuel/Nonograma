import pygame
from paquete.funciones_especificas import *
from graficos.config import *
pygame.init()

#Pantalla
rutas = ["Nonograma/archivos/auto.csv","Nonograma/archivos/buho.csv","Nonograma/archivos/cara_feliz.csv","Nonograma/archivos/gato.csv","Nonograma/archivos/inodoro.csv","Nonograma/archivos/hongo_malo.csv"]
ICONO = pygame.image.load("Nonograma/imagenes/icono_nonograma.png")
VENTANA = pygame.display.set_mode((ANCHO, ALTO))


pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)
activo = True
contador = 0
# dibujo_jugador = obtener_dibujo()
dibujo_jugador = obtener_dibujo(rutas)


while activo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("Se tocó cerrar")
            activo = False
    VENTANA.fill(GRIS)

    print(evento)
    pygame.draw.rect(VENTANA, 
                     BLANCO,
                     (X_INICIO, Y_INICIO, ANCHO_CUADRADO, ALTO_CUADRADO))
    
    medida = calcular_medida_celda(dibujo_jugador,(ANCHO_CUADRADO, ALTO_CUADRADO))

    resultado = medida[0]//2
    fuente = pygame.font.SysFont(None, int(resultado))
    pistas_fila = calcular_pistas_filas(dibujo_jugador)
    pistas_columna = calcular_pistas_columna(dibujo_jugador)


    # #DIBUJA CUADRADOS
    # dibujar_cuadrados_pygame(medida,(X_INICIO,Y_INICIO),VERDE,VENTANA,len(dibujo_jugador),medida[0])
    #ESTOY TESTEEANDO COMO QUEDA LA CRUZ DIBUJADA.
    funcion = dibujar("cruz")
    funcion((X_INICIO, Y_INICIO),GRIS,medida[0],VENTANA)
    # dibujar_cruz((X_INICIO, Y_INICIO),GRIS,medida[0],VENTANA)

    #TESTEANDO UN CUADRADO PINTADO.
    funcion = dibujar("cuadrado")
    funcion(medida,(X_INICIO + medida[0],Y_INICIO),AZUL,VENTANA)
    

    #DIBUJA LINEAS
    funcion = dibujar("linea vertical")
    dibujar_lineas((X_INICIO,Y_INICIO), medida[0],len(dibujo_jugador),NEGRO,VENTANA,funcion)
    funcion = dibujar("linea horizontal")
    dibujar_lineas((X_INICIO,Y_INICIO), medida[0],len(dibujo_jugador),NEGRO,VENTANA,funcion,True)
    
    #DIBUJA LAS PISTAS
    mostrar_pistas_filas_pygame(pistas_fila,(X_INICIO -25,Y_INICIO),VENTANA,fuente, NEGRO,medida[0])
    #DIBUJA LAS PISTAS DE LAS COLUMNAS.
    mostrar_pistas_columnas_pygame(pistas_columna,(X_INICIO, Y_INICIO - 25), VENTANA,fuente,NEGRO,medida[0])
    
    
    pygame.display.update()
pygame.quit()