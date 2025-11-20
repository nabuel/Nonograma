from .funciones_generales import *
from graficos.config import *
from .funciones_especificas import *
from .validaciones import *
import pygame

def calcular_pistas_filas(matriz: list)-> tuple:
    '''
    Calcula las pistas de las filas de la matriz.

    Parametros: "matriz" -> La matriz del nonograma.
    
    Retorno: La tupla con las pistas.
    '''
    pistas = []
    for i in range(len(matriz)):
        lista_pistas = calcular_pistas(matriz[i])
        pistas.append(lista_pistas)
    return tuple(pistas)


def calcular_pistas_columna(matriz: list)-> tuple:
    '''
    Calcula las pistas de las columnas de la matriz

    Parametros: "matriz" -> La matriz del nonograma.
    
    Retorno: La tupla con las pistas
    '''
    pistas = []
    for j in range(len(matriz[0])):
        columna = extraer_columna(matriz, j)
        lista_pistas = calcular_pistas(columna)
        pistas.append(lista_pistas)
    return tuple(pistas)


def calcular_pistas(lista: list)-> list:
    '''
    Calcula las pistas de la lista.

    Parametros: "lista" -> La lista a calcular las pistas.
    
    Retorno: Una lista con las pistas de la lista dada.
    '''
    contador = 0
    pistas = []
    for numero in lista:
        if numero == 0 and contador > 0:
            pistas.append(contador)
            contador = 0
        elif numero == 1:
            contador +=1
    
    if contador > 0:
        pistas.append(contador)

    return pistas 


def calcular_medida_celda(dibujo: list,
                          medida_cuadrado: tuple)-> tuple:
    '''
    Calcula las medidas de cada celda para el nonograma.
    
    Parametros: "dibujo" -> La matriz del nonograma.
                "medida_cuadrado" -> Las medidas del cuadrado donde se dibuja el nonograma.

    Retorno: Las medidas de ancho y largo.
    '''
    ancho = medida_cuadrado[0] // len(dibujo) 
    largo = medida_cuadrado[1] // len(dibujo[0])

    return ancho, largo


def calcular_puntuacion(tiempo: int,
                        vidas: int)-> int:
    '''
    Calcula la puntuación del jugador.
    
    Parametros: "tiempo" -> El tiempo que tardó el jugador en completar el nonograma.
                "vidas" -> Las vidas que le quedan al jugador.

    Retorno: El puntaje del jugador.
    '''
    puntaje = (vidas * 10000) // tiempo
    return puntaje


def dividir(dividendo: int|float,
            divisor: int|float)-> int|float:
    '''
    Divide al dividendo por el divisor
    
    Parametros: "dividendo" -> El número a dividir.
                "divisor" -> El número por el cual se divide.
    
    Retorno: El resultado de la división.
    '''
    resultado = dividendo / divisor

    return resultado


def calcular_datos_nonograma(rutas: list)-> tuple:
    '''
    Calcula los datos necesarios para el nonograma.

    PARAMETROS: "rutas" -> lista que contine las rutas de los dibujos.
    
    RETORNO: Los datos obtenidos.
    '''
    
    dibujo_jugador = obtener_dibujo(rutas)

    medida_casillas = calcular_medida_celda(dibujo_jugador,(ANCHO_GRILLA, ALTO_GRILLA))
    
    fuente = pygame.font.SysFont(None, int(medida_casillas[0]//2))

    pistas_fila = calcular_pistas_filas(dibujo_jugador)

    pistas_columna = calcular_pistas_columna(dibujo_jugador)

    longitud_casilla = medida_casillas[0]

    return dibujo_jugador,medida_casillas,fuente,pistas_fila,pistas_columna, longitud_casilla