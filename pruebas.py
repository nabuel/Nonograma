from paquete import funciones_especificas
from paquete import funciones_generales
from graficos.config import *

# #SELECCIONA EL DIBUJO.
# dibujo_correcto = funciones_especificas.obtener_dibujo()

# #Hace una grilla con el mismo tamaño del dibujo seleccionado.
# grilla_jugador = funciones_generales.crear_matriz(len(dibujo_correcto),len(dibujo_correcto[0]))

# #Estas son las medidas de cada celda para Pygame.
# medidas = funciones_especificas.calcular_medida_celda(grilla_jugador, (ANCHO_CUADRADO,ALTO_CUADRADO))

# ancho = medidas[0]
# largo = medidas[1]

# #Basandose en las coordendas de donde cliqueó el usuario. Las traduce a una coordenda de fila y columna para la grilla
# casilla_pintada = funciones_especificas.convertir_coordenada((354,452),(X_INICIO,Y_INICIO),ancho,dibujo_correcto)

# grilla_jugador = funciones_especificas.pintar_casilla(grilla_jugador,casilla_pintada,1)

# puntaje = funciones_especificas.calcular_puntuacion(13,3)
# matriz = funciones_generales.convertir_csv_matriz("Nonograma/archivos/ranking.csv")
# matriz_ordenada = funciones_especificas.ordenar_ranking(matriz)

# funciones_generales.escribir_csv("Nonograma/archivos/ranking.csv",matriz_ordenada,matriz[0])

funciones_especificas.mostrar_ranking("Nonograma/archivos/ranking.csv")

# funciones_especificas.dibujar_cruz((X_INICIO, Y_INICIO),VERDE,)