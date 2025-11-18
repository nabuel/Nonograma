import random
from .funciones_generales import *

def chequear_casilla(matriz_correcta: list,
                     fila: int,
                     columna: int,
                     dibujo: list)-> bool:
    '''
    Chequea si la casilla marcada es correcta.

    Retorno: True si es correcta.
             False si no lo es.
    '''
    if matriz_correcta[fila][columna] == dibujo[fila][columna]:
        return True

    return False

def chequear_dibujo_terminado(dibujo: list,
                             respuesta: list)-> bool:
    '''
    Chequea si el dibujo fué completado correctamente.

    Retorno: True si fué completado correctamente.
             False si no fué completado correctamente.
    '''
    for i in range(len(dibujo)):
        for j in range(len(dibujo[i])):
            if dibujo[i][j] != respuesta[i][j]:
                return False
    
    return True

def get_int(mensaje: str)-> int:
    '''
    Consigue un número entero positivo.

    Retorno: el número entero conseguido.
    '''
    numero = input(mensaje)

    while not numero.isdigit():
        print("Se le solicita ingresar número entero positivo.")
        numero = input(mensaje)
    
    return int(numero)

def get_coordenada(mensaje_fila: str,
                   mensaje_columna: str,
                   matriz:list)-> tuple:
    '''
    Obtiene una coordenada para una matriz.

    Retorno: una tupla con las coordenas obtenidas.
    '''
    fila = get_int(mensaje_fila)
    columna = get_int(mensaje_columna)
    
    while not validar_coordenada(fila,columna,matriz):
        fila = get_int(mensaje_fila)
        columna = get_int(mensaje_columna)
    
    return fila,columna

def validar_coordenada(fila: int,
                       columna: int,
                       matriz: list)-> bool:
    '''
    Valida si la coordenada existe dentro de la matriz.

    Retorno: True si son válidas.
             False si no lo son.
    '''
    if fila > len(matriz):
        return False
    elif columna > len(matriz[0]):
        return False

    return True

def obtener_dibujo(lista_rutas: list)-> list:
    '''
    Obtiene un dibujo al azar.

    Retorno: el dibujo seleccionado
    '''
    numero_dibujo = random.randint(0,len(lista_rutas)-1)
    dibujo = convertir_csv_matriz(lista_rutas[numero_dibujo])
    
    # match numero_dibujo:
    #     case 1:
    #         ruta = "Nonograma/archivos/auto.csv"
    #     case 2:
    #         ruta = "Nonograma/archivos/buho.csv"
    #     case 3:
    #         ruta = "Nonograma/archivos/cara_feliz.csv"
    #     case 4:
    #         ruta = "Nonograma/archivos/gato.csv"
    #     case 5:
    #         ruta = "Nonograma/archivos/inodoro.csv"
    #     case 6:
    #         ruta = "Nonograma/archivos/hongo_malo.csv"
        
    # dibujo = convertir_csv_matriz(ruta)

    return dibujo

def validar(tipo: str)-> any:
    '''
    Hace la validación según el tipo ingresado.

    Retorno: la función elegida.
    '''
    match tipo:
        case "coordenada":
            funcion = validar_coordenada
        case "casilla":
            funcion = chequear_casilla
        case "dibujo":
            funcion = chequear_dibujo_terminado
    
    return funcion

def obtener_dato(tipo: str)->any:
    '''
    Busca la función para obtener el tipo de dato.

    Retorno: La función seleccionada.
    '''
    match tipo:
        case "entero":
            funcion = get_int
        case "coordenada":
            funcion = get_coordenada
        case "string":
            funcion = input
        case "dibujo":
            funcion = obtener_dibujo
    
    return funcion

