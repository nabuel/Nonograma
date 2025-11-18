from .validaciones import *
from .funciones_generales import *
import pygame


def calcular_pistas_filas(matriz: list)-> tuple:
    '''
    Calcula las pistas de las filas de la matriz.

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

    Retorno: Una lista con las pistas de la lista dada.
    '''
    contador = 0
    pistas = []
    for numero in lista:
        if numero == 0 and contador > 0:
            pistas.append(contador)
            contador = 0
        elif numero != 0:
            contador +=1
    
    if contador > 0:
        pistas.append(contador)

    return pistas 

def chequear_final(dibujo: list,
                   vidas: int,
                   respuesta: str)-> bool:
    '''
    Chequea si se sigue jugando o no.

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

def pintar_casilla(dibujo: list,
                   coordenada: tuple,
                   valor = False)-> list:
    '''
    Pinta la casilla ubicada en las coordenadas de fila y columna.

    Retorno: El dibujo con la casilla pintada.
    '''
    fila = coordenada[0]
    columna = coordenada[1]

    dibujo[fila][columna] = valor
    
    return dibujo


# def extraer_funcion(lista_funciones: list,
#                     indice: int)-> any:
#     '''
#     Selecciona la función indicada de la lista de funciones.

#     Retorno: la funcion seleccionada.
#     '''
#     funcion = lista_funciones[indice]
#     return funcion

def calcular_medida_celda(dibujo: list,
                          medida_cuadrado: tuple)-> tuple:
    '''
    Calcula las medidas de cada celda para el nonograma.

    Retorno: Las medidas de ancho y largo.
    '''
    ancho =  medida_cuadrado[0] / len(dibujo)
    largo = medida_cuadrado[1] / len(dibujo[0])

    return ancho, largo

def dibujar_linea_vertical(inicio: tuple,
                           aumento: int,
                           repeticiones: int,
                           color: tuple,
                           superficie: any)-> None:
    '''
    Dibuja una linea vertical de la medidas indicadas. Dentro de Pygame.
    '''
    x= inicio[0]
    y = inicio[1]
    i = 0
    while i < repeticiones:
        pygame.draw.line(superficie, 
                        color,
                        (x, y),(x,y + aumento),2)
        y += aumento
        i += 1

# def dibujar_lineas_verticales(inicio: tuple,
#                               aumento: int,
#                               repeticiones: int,
#                               color: tuple,
#                               superficie: any)-> None:
#     '''
#     Dibuja varias lineas verticales en la superficie indicada. Dentro de Pygame.
#     '''
#     x= inicio[0]
#     y = inicio[1]
#     funcion = dibujar("linea vertical")
#     for _ in range(repeticiones + 1):
#         funcion((x, y), aumento, repeticiones,color, superficie)
#         x += aumento


def dibujar_lineas(inicio: tuple,
                    aumento: int,
                    repeticiones: int,
                    color: tuple,
                    superficie: any,
                    funcion: function,
                    sentido= False)->None:
    '''
    Dibuja varias lineas en el sentido indicado

    PARAMETROS: "inicio"-> Punto de inicio de la linea.
                
                "color" -> color de la linea.
                
                "repeticiones" -> la cantidad de veces que se ejecutará el proceso.
                
                "superficie"-> la superficie donde será pintada las lineas.
                
                "funcion"-> funcion que debe dibujar la linea.
                
                "sentido" -> orientación en la cual se dibujan las lineas. Si sentido = False se incrementa el "x" para dibujar lineas verticales. En caso de que sentido = True se incrementa el eje "y" para dibujar lineas horizontales
    '''
    x= inicio[0]
    y = inicio[1]

    for _ in range(repeticiones + 1):
        funcion((x, y), aumento, repeticiones,color, superficie)
        if sentido:
            y += aumento
        else:
            x += aumento


# def dibujar_lineas_horizontales(inicio: tuple,
#                                 aumento: int,
#                                 repeticiones: int,
#                                 color: tuple,
#                                 superficie: any)-> None:
#     '''
#     Dibuja varias lineas verticales en Pygame.
#     '''
#     x= inicio[0]
#     y = inicio[1]
#     for _ in range(repeticiones +1):
#         dibujar_linea_horizontal((x, y), aumento, repeticiones,color, superficie)
#         y += aumento



def dibujar_linea_horizontal(inicio: tuple,
                             aumento: int,
                             repeticiones: int,
                             color: tuple,
                             superficie: any)-> None:
    '''
    Dibuja una linea vertical en Pygame.
    '''
    x= inicio[0]
    y = inicio[1]
    i = 0
    while i < repeticiones:
        pygame.draw.line(superficie, 
                        color,
                        (x, y),(x + aumento,y),2)
        x += aumento
        i += 1



def dibujar_cuadrado_pygame(medidas:tuple,
                     coordenada_inicio: tuple,
                     color: tuple,
                     superficie: any):
    '''
    Dibuja un cuadrado en la posición indicada con Pygame.
    '''
    pygame.draw.rect(superficie,color,(coordenada_inicio[0],coordenada_inicio[1],medidas[0], medidas[1]))

def dibujar_cuadrados_pygame(medidas_cuadrado:tuple,
                     coordenada_inicio: tuple,
                     color: tuple,
                     superficie: any,
                     repeticiones: int,
                     aumento: int)-> None:
    '''
    Dibuja varios cuadrados con Pygame.

    PARAMETROS: "medidas_cuadrado"-> Son las medidas del cuadrado por ejemplo (400,400)
                "coordenada_inicio" -> es la coordenada de la punta superior izquierda del cuadrado.
                "color" -> color del cuadrado.
                "superficie"-> la superficie donde será pintado el cuadrado.
                "aumento"-> es el valor por el cual los ejes irán aumentado.
    '''
    x = coordenada_inicio[0]
    y = coordenada_inicio[1]

    for i in range(repeticiones):
        for j in range(repeticiones):
            dibujar_cuadrado_pygame(medidas_cuadrado,(x,y),color,superficie)
            x += aumento
        y += aumento
        x = coordenada_inicio[0]


def convertir_coordenada_columna(coordenada: tuple, 
                        coordenada_inicial: tuple, 
                        aumento: int, 
                        matriz: list)->int:
    '''
    Traduce el valor de la coordenada en el valor de la columna de la matriz ingresada.

    PARAMETROS: "coordenada" -> valor de la coordenada cliqueada.
                "coordenada_inicial" -> coordenada de la esquina superior izquierda del cuadrado/rectángulo.
                "aumento" -> el valor con el cual fué aumentando el valor de x
                "matriz": -> matriz donde se encuentra el nonograma de forma lógica.
    Retorno: El valor de la columna.
             Si el valor es -1 es que esa coordenada no está dentro de la matriz.
    '''
    x = coordenada[0]
    x_inicial = coordenada_inicial[0]


    for i in range(len(matriz)):
        resultado = x_inicial + aumento
        if x == x_inicial:
            return i
        elif resultado > x:
            return i
        else:
            x_inicial += aumento
    
    return -1

def convertir_coordenada_fila(coordenada: tuple, 
                        coordenada_inicial: tuple, 
                        aumento: int, 
                        matriz: list)->int:
    '''
    Traduce el valor de la coordenada en el valor de la fila de la matriz ingresada.

    PARAMETROS: "coordenada" -> valor de la coordenada cliqueada.
                "coordenada_inicial" -> coordenada de la esquina superior izquierda del cuadrado/rectángulo.
                "aumento" -> el valor con el cual fué aumentando el valor de y
                "matriz": -> matriz donde se encuentra el nonograma de forma lógica.
    
    Retorno: El valor de la fila.
             Si el valor es -1 es que esa coordenada no está dentro de la matriz.
    '''
    y = coordenada[1]
    y_inicial = coordenada_inicial[1]


    for i in range(len(matriz)):
        resultado = y_inicial + aumento
        if y == y_inicial:
            return i
        elif resultado > y:
            return i
        else:
            y_inicial += aumento
    
    return -1

def convertir_coordenada(coordenada: tuple, 
                        coordenada_inicial: tuple, 
                        aumento: int, 
                        matriz: list)->int:
    '''
    Convierte la coordenada en un valor de fila y columna para la matriz ingresada.
    
    PARAMETROS: "coordenada" -> valor de la coordenada cliqueada.
                "coordenada_inicial" -> coordenada de la esquina superior izquierda del cuadrado/rectángulo.
                "aumento" -> el valor con el cual fué aumentando el valor de y
                "matriz": -> matriz donde se encuentra el nonograma de forma lógica. 
    '''
    funcion = obtener_funcion_coordenda("fila")
    fila = funcion(coordenada, coordenada_inicial,aumento,matriz)
    funcion = obtener_funcion_coordenda("columna")
    columna = funcion(coordenada, coordenada_inicial, aumento,matriz)

    return fila,columna


def obtener_funcion_coordenda(tipo: str)->None:
    '''
    obtiene la funcion para convertir una coordenada en un valor de fila o columna.
    
    PARAMETROS: "tipo" -> indica si quiere la conversión de las filas o columnas.

    Retorno: La funcion seleccionada ó None en caso de que no exista
    '''
    match tipo.lower():
        case "fila":
            funcion = convertir_coordenada_fila
        case "columna":
            funcion = convertir_coordenada_columna
        case _:
            funcion = None
        
    return funcion 


def mostrar_pistas_filas_pygame(lista_pistas: tuple,
                        coordenadas: tuple,
                        superficie: any,
                        fuente: int|float,
                        color: tuple,
                        aumento: int)-> None:
    '''
    Muestra la pista en Pygame.
    '''
    funcion = dividir
    y = coordenadas[1]
    y = y + funcion(2,aumento)

    for pista in lista_pistas:
        indice = -1
        x = coordenadas[0]
        for i in range(len(pista)):
            texto = fuente.render(str(pista[indice]),True, color)
            if pista[i] > 9:
                superficie.blit(texto, (x-5,y))
            else:
                superficie.blit(texto, (x,y))
            indice -= 1
            
            x -= funcion(2,aumento)
        y += aumento

def mostrar_pistas_columnas_pygame(lista_pistas: tuple,
                        coordenadas: tuple,
                        superficie: any,
                        fuente: int|float,
                        color: tuple,
                        aumento: int)-> None:
    '''
    Muestra las pistas en Pygame.
    '''
    funcion = dividir
    x = coordenadas[0]
    x = x + funcion(2,aumento)

    for pista in lista_pistas:
        indice = -1
        y = coordenadas[1]
        for i in range(len(pista)):
            texto = fuente.render(str(pista[indice]),True, color)
            if pista[i] > 9:
                superficie.blit(texto, (x - 5,y))
            else:
                superficie.blit(texto, (x,y))
            indice -= 1
            y -= funcion(2, aumento)
        x += aumento

def calcular_puntuacion(tiempo: int,
                        vidas: int)-> int:
    '''
    Calcula la puntuación del jugador.

    Retorno: El puntaje del jugador.
    '''
    puntaje = (vidas * 10000) // tiempo
    return puntaje

def ordenar_ranking(ranking: list):
    '''
    Ordena el ranking de mayor a menor.

    Retorno: El ranking ordenado.
    '''
    lista = []
    for i in range(1,len(ranking)):
        lista.append(ranking[i][2])
    
    lista.sort(reverse=True)

    ranking_retorno = []
    for elemento in lista:
        for i in range(1, len(ranking)):
            if elemento == ranking[i][2]:
                ranking_retorno.append(ranking[i])
                break
    
    return ranking_retorno

def mostrar_ranking(ruta: str,
                    limite: int)-> None:
    '''
    Muestra los primeros 10 jugadores del ranking.
    '''
    matriz = convertir_csv_matriz(ruta)

    for i in range(len(matriz)):
        if i > limite:
            break
        for j in range(len(matriz[i])):
            distancia = len(matriz[0][0]) // 2
            print(matriz[i][j],"" * distancia, end="")
        print("")

def dibujar_cruz(inicio: tuple,
                color: tuple,
                longitud_cruz: int|float,
                superficie: any)-> None:
    '''
    Dibuja una linea vertical en Pygame.
    
    PARAMETROS: "inicio"-> Punto de inicio de la cruz.
                "color" -> color de la cruz.
                "superficie"-> la superficie donde será pintado la cruz.
                "longitud_cruz"-> longitud de la cruz.
    '''
    x= inicio[0]
    y = inicio[1]

    #DIBUJA UNA LINEA DE LA ESQUINA SUPERIOR IZQUIERDA DEL CUADRADO A LA ESQUINA INFERIOR DERECHA.
    pygame.draw.line(superficie, 
                        color,
                        (x, y),(x + longitud_cruz,y+longitud_cruz),3)
    
    #DIBUJA UNA LINEA DE LA ESQUINA INFERIOR IZQUIERDA DEL CUADRADO A LA ESQUINA SUPERIOR DERECHA.
    pygame.draw.line(superficie, 
                        color,
                        (x, y+longitud_cruz),(x + longitud_cruz,y),3)

def dibujar(figura: str)-> function|None:
    '''
    Busca la función para dibujar la figura solicitada.

    PARAMETROS: "figura" -> la figura a dibujar.
    
    RETORNO: La función para dibujar la figura.
    '''
    match figura.lower():
        case "cuadrado":
            funcion = dibujar_cuadrado_pygame
        case "linea vertical":
            funcion = dibujar_linea_vertical
        case "linea horizontal":
            funcion = dibujar_linea_horizontal
        case "cruz":
            funcion = dibujar_cruz
        case _:
            funcion = None

    return funcion