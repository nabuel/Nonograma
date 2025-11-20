
from .validaciones import *
from .funciones_generales import *
from .calculos import *
# import Pygame


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


def dibujar_lineas(inicio: tuple,
                    aumento: int,
                    repeticiones: int,
                    color: tuple,
                    superficie: any,
                    funcion: any,
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


def dibujar_cuadrados_especificos(lista_coordenadas: list,
                                medidas_cuadrado:tuple,
                                color: tuple,
                                superficie: any)-> None:
    '''
    Dibuja varias cuadrados en las ubicaciones especificas indicadas.

    PARAMETROS: "lista_coordenadas" -> es una lista que contiene las coordendas de los cuadrados especificos a pintar.
                "medidas_cuadrado" -> Son las medidas del cuadrado
                "coordenada_inicio" -> es la coordenada de la punta superior izquierda del cuadrado.
                "color" -> color del cuadrado.
                "superficie" -> la superficie donde será pintado el cuadrado.
                "aumento" -> es el valor por el cual los ejes irán aumentado.
    '''
    for coordenada in lista_coordenadas:
        dibujar_cuadrado_pygame(medidas_cuadrado,(coordenada[0],coordenada[1]),color,superficie)


def calcular_inicio_cuadrado(posicion_click: tuple,
                    aumento: int,
                    coordenada_inicial:tuple)-> tuple:
    '''
    Según donde se clickea se calcula la coordenada de inicio del cuadrado.

    PARAMETROS: "posicion_click" -> coordenada donde se cliqueó.
                "aumento" -> la longitud del cuadrado.
                "coordenda_inicial" -> coordenda donde se inició la grilla.
    '''
    x = posicion_click[0]
    x_inicio = coordenada_inicial[0]

    y = posicion_click[1]
    y_inicio = coordenada_inicial[1]

    while x != x_inicio or y != y_inicio:
        if x < x_inicio + aumento:
            x = int(x_inicio)
        elif x == x_inicio:
            pass
        else:
            x_inicio += aumento

        if y < y_inicio + aumento:
            y = y_inicio
        elif y == int(y_inicio):
            pass
        else:
            y_inicio += aumento

    return x,y


def convertir_coordenada(coordenada: tuple,
                        coordenada_inicial: tuple,
                        aumento: int,
                        matriz: list,
                        sentido=False)-> int:
    '''
    Convierte la coordenada en un valor de fila y columna para la matriz ingresada.
    
    PARAMETROS: "coordenada" -> valor de la coordenada cliqueada.
                "coordenada_inicial" -> coordenada de la esquina superior izquierda del cuadrado/rectángulo.
                "aumento" -> el valor con el cual fué aumentando el valor de y
                "matriz" -> matriz donde se encuentra el nonograma de forma lógica.
                "sentido" -> cuando es true se convierte la coordenada de la fila. En caso de que sea False convierte la coordenada de la columna.
    
    RETORNO: El valor de la fila ó de la columna según el sentido.
             Si el valor es -1 es que esa coordenada no está dentro de la matriz.
    '''
    if sentido: #Para la fila.
        eje = coordenada[1]
        eje_inicial = coordenada_inicial[1]
    else:
        eje = coordenada[0]
        eje_inicial = coordenada_inicial[0]


    for i in range(len(matriz)):
        resultado = eje_inicial + aumento
        if eje == eje_inicial:
            return i
        elif resultado > eje:
            return i
        else:
            eje_inicial += aumento
    
    return -1


def convertir_coordenadas(coordenada: tuple, 
                        coordenada_inicial: tuple, 
                        aumento: int, 
                        matriz: list)->tuple:
    '''
    Convierte la coordenada en un valor de fila y columna para la matriz ingresada.
    
    PARAMETROS: "coordenada" -> valor de la coordenada cliqueada.
                "coordenada_inicial" -> coordenada de la esquina superior izquierda del cuadrado/rectángulo.
                "aumento" -> el valor con el cual fué aumentando el valor de y
                "matriz": -> matriz donde se encuentra el nonograma de forma lógica. 
    
    RETORNO: Las coordenada obtenidas para la matriz.
    '''
    fila = convertir_coordenada(coordenada, coordenada_inicial,aumento,matriz,True)
    columna = convertir_coordenada(coordenada, coordenada_inicial, aumento,matriz)

    return fila,columna


def mostrar_pistas_filas_pygame(lista_pistas: tuple,
                        coordenadas: tuple,
                        superficie: any,
                        fuente: int|float,
                        color: tuple,
                        aumento: int)-> None:
    '''
    Muestra la pista en Pygame.
    '''
    y = coordenadas[1]
    y = y + dividir(aumento,2)

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
            
            x -= dividir(aumento,2)
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
    x = x + funcion(aumento,2)

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
            y -= funcion(aumento,2)
        x += aumento


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






def dibujar_cruces_especificas(lista_coordenadas: list,
                                longitud_cruz: int|float,
                                color: tuple,
                                superficie: any)-> None:
    '''
    Dibuja varias cruces en las ubicaciones especificas indicadas.

    PARAMETROS: "lista_coordenadas" -> es una lista que contiene las coordendas de las cruces especificas a pintar.
                "longitud_cruz"-> longitud de la cruz.
                "color" -> color de la cruz.
                "superficie" -> la superficie donde será pintado la cruz.
    '''
    dibujar_cruz = dibujar("cruz")
    for coordenada in lista_coordenadas:
        dibujar_cruz((coordenada[0],coordenada[1]),color,longitud_cruz,superficie)


def dibujar(figura: str)-> None:
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
            funcion = dibujar_cruz_pygame
        case _:
            funcion = None

    return funcion


def dibujar_cruz_pygame(inicio: tuple,
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
    x = inicio[0]
    y = inicio[1]
    
        #DIBUJA UNA LINEA DE LA ESQUINA SUPERIOR IZQUIERDA DEL CUADRADO A LA ESQUINA INFERIOR DERECHA.
    pygame.draw.line(superficie, 
                        color,
                        (x, y),(x + longitud_cruz,y+longitud_cruz),3)
    
    #DIBUJA UNA LINEA DE LA ESQUINA INFERIOR IZQUIERDA DEL CUADRADO A LA ESQUINA SUPERIOR DERECHA.
    pygame.draw.line(superficie, 
                        color,
                        (x, y+longitud_cruz),(x + longitud_cruz,y),3)


def cargar_coordenadas_grilla(grilla_jugador: list,
                              longitud_casilla: int,
                              coordenadas_inicio: tuple) -> list:
    '''
    Carga la matriz con las coordenadas de las casillas.
    
    PARAMETROS: "grilla_jugador" -> grilla lógica del jugador.

                "longitud_casilla" -> logitud de las casillas para calcular las coordenadas.
                
                "coordenadas_inicio" -> Esquina superior izquierda de la grilla dibujada.
    
    RETORNO: La matriz cargada con las coordenadas iniciales de las casillas.
    '''
    matriz_retorno = []
    x,y = coordenadas_inicio
    for i in range(len(grilla_jugador)):
        for _ in range(len(grilla_jugador[i])):
            matriz_retorno.append((x,y))
            x += longitud_casilla
        y += longitud_casilla
        x = coordenadas_inicio[0]
    
    return matriz_retorno


def definir_estado_click(posicion_click: tuple,
                        grilla_jugador: list,
                        longitud_casilla: int,
                        numero_click: int,
                        grilla_correcta: list,
                        coordenadas_correctas: set) -> str:
    '''
    Define el estado del click realizado por el jugador.
    
    PARAMETROS: "posicion_click" -> coordenada donde se cliqueó.
                "grilla_jugador" -> grilla lógica del jugador.
                "longitud_casilla" -> logitud de las casillas para calcular las coordenadas.
                "numero_click" -> número del click realizado (1 = izquierdo, 3 = derecho).
    
    RETORNO: El estado del click (correcto, incorrecto, revertir).
    '''
    #click izquierdo
    fila,columna = convertir_coordenadas(posicion_click, (X_INICIO_GRILLA,Y_INICIO_GRILLA), longitud_casilla,grilla_jugador)
    if numero_click == 1:
        
        if grilla_jugador[fila][columna] == 1 and (posicion_click not in coordenadas_correctas):
            estado = "borrar"
        elif grilla_jugador[fila][columna] == 0 and (posicion_click not in coordenadas_correctas):
            estado = "revertir"
        elif grilla_correcta[fila][columna] == 1:
            estado = "correcto"
        elif grilla_correcta[fila][columna] == 0:
            estado = "incorrecto"
    
    elif numero_click == 3:
        
        if grilla_jugador[fila][columna] == 0 and (posicion_click not in coordenadas_correctas):
            estado = "borrar"
        elif grilla_jugador[fila][columna] == 1 and (posicion_click not in coordenadas_correctas):
            estado = "revertir"
        elif grilla_correcta[fila][columna] == 0:
            estado = "correcto"
        elif grilla_correcta[fila][columna] == 1:
            estado = "incorrecto"
    
    return estado
    
        
def manejar_click(numero_click: int,
                 estado_click: str,
                 set_coordenadas_correctas: set,
                 lista_coordenadas_suspendidas: list,
                 coordenadas_cruz: set,
                 coordenadas_cuadrado: set,
                 posicion_click: tuple)-> tuple:
    '''
    Maneja el click realizado por el jugador.
    
    PARAMETROS: "numero_click" -> número del click realizado (1 = izquierdo, 3 = derecho).
                "estado_click" -> el estado del click (correcto, incorrecto, revertir).
                "set_coordenadas_correctas" -> conjunto de coordenadas correctas.
                "lista_coordenadas_suspendidas" -> lista de coordenadas suspendidas.
                "coordenadas_cruz" -> conjunto de coordenadas donde se dibuja una cruz.
                "coordenadas_cuadrado" -> conjunto de coordenadas donde se dibuja un cuadrado.
                "posicion_click" -> coordenada donde se cliqueó.
    '''

    match estado_click:
        case "correcto":
            if numero_click == 1:
                coordenadas_cuadrado.add(posicion_click)
            elif numero_click == 3:
                coordenadas_cruz.add(posicion_click)
                
            set_coordenadas_correctas.add(posicion_click)
        case "incorrecto":
            if numero_click == 1:
                if lista_coordenadas_suspendidas.count(posicion_click) == 0:
                    lista_coordenadas_suspendidas.append(posicion_click)
    
                coordenadas_cuadrado.add(posicion_click)
            elif numero_click == 3:
                if lista_coordenadas_suspendidas.count(posicion_click) == 0:
                    lista_coordenadas_suspendidas.append(posicion_click)
                
                coordenadas_cruz.add(posicion_click)
                
        case "revertir":
            if numero_click == 1:
                coordenadas_cruz.discard(posicion_click)
                coordenadas_cuadrado.add(posicion_click)
            elif numero_click == 3:
                coordenadas_cruz.add(posicion_click)
                coordenadas_cuadrado.discard(posicion_click)
            
            set_coordenadas_correctas.add(posicion_click)
            lista_coordenadas_suspendidas.remove(posicion_click)
        
        case "borrar":
            if numero_click == 1:
                coordenadas_cuadrado.discard(posicion_click)
            elif numero_click == 3:
                coordenadas_cruz.discard(posicion_click)
            
            lista_coordenadas_suspendidas.remove(posicion_click)
            
    return set_coordenadas_correctas, lista_coordenadas_suspendidas, coordenadas_cruz, coordenadas_cuadrado