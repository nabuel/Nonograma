import random
from .funciones_generales import *
from graficos.config import *

def chequear_casilla(matriz_correcta: list,
                     coordenadas: tuple,
                     dibujo: list)-> bool:
    '''
    Chequea si la casilla marcada es correcta.
    
    Parametros: "matriz_correcta" -> La matriz correcta del nonograma.
                "coordenadas" -> Las coordenadas a chequear.
                "dibujo" -> La matriz del jugador.

    Retorno: True si es correcta.
             False si no lo es.
    '''
    fila, columna = coordenadas
    if matriz_correcta[fila][columna] == dibujo[fila][columna]:
        return True
    return False


def chequear_dibujo_terminado(dibujo: list,
                             respuesta: list)-> bool:
    '''
    Chequea si el dibujo fué completado correctamente.
    
    Parametros: "dibujo" -> La matriz del jugador.
                "respuesta" -> La matriz correcta del nonograma.

    Retorno: True si fué completado correctamente.
             False si no fué completado correctamente.
    '''
    contador_respuesta = 0
    contador = 0
    
    for i in range(len(dibujo)):
        contador_respuesta += respuesta[i].count(1)
        for j in range(len(dibujo[i])):
            if dibujo[i][j] == 1 and respuesta[i][j] == 1:
                contador += 1
    
    if contador_respuesta == contador:
        return True
    else:
        return False


def get_coordenada(mensaje_fila: str,
                   mensaje_columna: str,
                   matriz:list)-> tuple:
    '''
    Obtiene una coordenada para una matriz.
    
    Parametros: "mensaje_fila" -> El mensaje para pedir la fila.
                "mensaje_columna" -> El mensaje para pedir la columna.
                "matriz" -> La matriz donde se van a usar las coordenadas.

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
    
    Parametros: "fila" -> La fila a validar.
                "columna" -> La columna a validar.
                "matriz" -> La matriz donde se van a validar las coordenadas.

    Retorno: True si son válidas.
             False si no lo son.
    '''
    if fila >= len(matriz):
        return False
    elif columna >= len(matriz[0]):
        return False

    return True


def obtener_dibujo(lista_rutas: list)-> list:
    '''
    Obtiene un dibujo al azar.
    
    Parametros: "lista_rutas" -> La lista con las rutas de los dibujos.

    Retorno: el dibujo seleccionado
    '''
    numero_dibujo = random.randint(0,len(lista_rutas)-1)
    dibujo = convertir_csv_matriz(lista_rutas[numero_dibujo])

    return dibujo


def validar(tipo: str)-> any:
    '''
    Hace la validación según el tipo ingresado.
    
    Parametros: "tipo" -> El tipo de validación a realizar.

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
    
    Parametros: "tipo" -> El tipo de dato a obtener.

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


def chequear_final(dibujo: list,
                   vidas: int,
                   respuesta: str)-> bool:
    '''
    Chequea si se sigue jugando o no.

    Parametros: "dibujo" -> La matriz del jugador.
                "vidas" -> Las vidas que le quedan al jugador.
                "respuesta" -> La matriz correcta del nonograma.
    
    Retorno: True si se sigue jugando.
             False si no se sigue jugandno.
    '''
    seguir_jugando = False
    if vidas == 0:
        print("Te quedaste sin vidas.")
        print("")
    elif chequear_dibujo_terminado(dibujo, respuesta):
        print("GANASTE!! Completaste correctamente el dibujo.")
        print("")
    else:
        seguir_jugando = True
    
    return seguir_jugando


def validar_click_grilla(posicion_mouse: tuple)-> bool:
    '''
    Verifica si la coordenada del mouse está dentro de la grilla del Nonograma.
    
    Parametros: "posicion_mouse" -> La posición del mouse.
    
    Retorno: True si está dentro de la grilla.
             False si no lo está.
    '''
    x,y = posicion_mouse
    bandera = True

    if x < X_INICIO_GRILLA or x > X_INICIO_GRILLA + ANCHO_GRILLA - 2:
        bandera = False
    elif y < Y_INICIO_GRILLA or y > Y_INICIO_GRILLA + ALTO_GRILLA:
        bandera = False
    
    return bandera