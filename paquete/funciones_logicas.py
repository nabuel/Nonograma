from .funciones_graficas import *
from .calculos import *
from .validaciones import *


def pintar_casilla(dibujo: list,
                   coordenada: tuple,
                   valor = False)-> list:
    '''
    Pinta la casilla ubicada en las coordenadas de fila y columna.

    Parametros: "dibujo" -> dibujo donde se pintará la casilla.
                "coordenada" -> coordenada de la casilla a pintar.
                "valor" -> valor con el cual se pintará la casilla.
    
    Retorno: El dibujo con la casilla pintada.
    '''
    fila = coordenada[0]
    columna = coordenada[1]

    dibujo[fila][columna] = valor
    
    return dibujo



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


def convertir_coordenadas_matriz(coordenada: tuple, 
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


def ordenar_ranking(ranking: list):
    '''
    Ordena el ranking de mayor a menor.
    
    Parametros: "ranking" -> matriz que contiene el ranking de los jugadores.

    Retorno: El ranking ordenado.
    '''

    lista = []
    for i in range(1,len(ranking)):
        lista.append(ranking[i][3])
    
    lista.sort(reverse=True)

    ranking_retorno = []
    for elemento in lista:
        for i in range(1, len(ranking)):
            if elemento == ranking[i][3]:
                ranking_retorno.append(ranking[i])
                break
    
    return ranking_retorno


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
                "grilla_correcta" -> grilla lógica correcta del nonograma.
                "coordenadas_correctas" -> conjunto de coordenadas correctas.
    
    RETORNO: El estado del click (correcto, incorrecto, revertir).
    '''
    #click izquierdo
    fila,columna = convertir_coordenadas_matriz(posicion_click, (X_INICIO_GRILLA,Y_INICIO_GRILLA), longitud_casilla,grilla_jugador)
    celda_jugador = grilla_jugador[fila][columna]
    celda_correcta = grilla_correcta[fila][columna]
    
    estado = ""
    match numero_click:
        case 1:
            if celda_correcta == 1:
                estado = "correcto"
            elif celda_correcta == 0 and celda_jugador not in coordenadas_correctas:
                estado = "incorrecto"

        case 3:    
                if celda_correcta == 0:
                    estado = "correcto"
                elif celda_correcta == 1 and celda_jugador not in coordenadas_correctas:
                    estado = "incorrecto"

            
    return estado


def manejar_click(numero_click: int,
                 estado_click: str,
                 set_coordenadas_correctas: set,
                 set_coordenadas_cruz: set,
                 set_coordenadas_cuadrado: set,
                 posicion_click: tuple)-> tuple:
    '''
    Maneja el click realizado por el jugador.
    
    PARAMETROS: "numero_click" -> número del click realizado (1 = izquierdo, 3 = derecho).
                "estado_click" -> el estado del click (correcto, incorrecto, revertir).
                "set_coordenadas_correctas" -> conjunto de coordenadas correctas.
                "set_coordenadas_cruz" -> conjunto de coordenadas donde se dibuja una cruz.
                "set_coordenadas_cuadrado" -> conjunto de coordenadas donde se dibuja un cuadrado.
                "posicion_click" -> coordenada donde se cliqueó.
    
    RETORNO: Los conjuntos de coordenadas actualizados.
    '''

    match estado_click:
        case "correcto":
            if numero_click == 1:
                set_coordenadas_cuadrado.add(posicion_click)
                set_coordenadas_cruz.discard(posicion_click)

            elif numero_click == 3:
                set_coordenadas_cuadrado.discard(posicion_click)
                set_coordenadas_cruz.add(posicion_click)

            set_coordenadas_correctas.add(posicion_click)
        case "incorrecto":
            if posicion_click not in set_coordenadas_correctas:
                if numero_click == 1:
                    set_coordenadas_cuadrado.add(posicion_click)
                elif numero_click == 3:
                    set_coordenadas_cruz.add(posicion_click)
        
    return set_coordenadas_correctas, set_coordenadas_cruz, set_coordenadas_cuadrado


def buscar_casilla_erronea(matriz_jugador: list,
                           matriz_correcta: list)-> tuple |None:
    '''
    Busca una casilla erronea en la grilla del jugador.
    
    PARAMETROS: "matriz_jugador" -> grilla lógica del jugador.
                "matriz_correcta" -> grilla lógica correcta del nonograma.

    Retorno: La fila y columna de la casilla erronea. En caso de no encontrar ninguna retorna None.
    '''
    for i in range(len(matriz_jugador)):
        for j in range(len(matriz_jugador[i])):
            if matriz_jugador[i][j] != None:
                if matriz_jugador[i][j] != matriz_correcta[i][j]:
                    return i,j
    
    return None


def invertir_cuadrado(valor_click: int)-> int:
    '''
    Invierte el valor del cuadrado.
    
    PARAMETROS: "valor_click" -> valor del click realizado (1 = izquierdo, 3 = derecho).

    Retorno: El valor invertido.
    '''
    if valor_click == 1:
        return 0
    elif valor_click == 3:
        return 1


def arreglar_coordenadas_pygame(valor_click: int,
                              posicion_click: tuple,
                              set_coordenadas_cruz: set,
                              set_coordenadas_cuadrado: set)-> tuple:
    '''
    Arregla las listas de coordenadas según el click realizado.
    
    Parametros: "valor_click" -> valor del click realizado (1 = izquierdo, 3 = derecho).
                "posicion_click" -> coordenada donde se cliqueó.
                "set_coordenadas_cruz" -> conjunto de coordenadas donde se dibuja una cruz.
                "set_coordenadas_cuadrado" -> conjunto de coordenadas donde se dibuja un cuadrado.

    Retorno: Las listas arregladas.
    '''
    match valor_click:
        case 1:
            set_coordenadas_cuadrado.discard(posicion_click)
            set_coordenadas_cruz.add(posicion_click)
        case 3:
            set_coordenadas_cuadrado.add(posicion_click)
            set_coordenadas_cruz.discard(posicion_click)
    
    return set_coordenadas_cruz, set_coordenadas_cuadrado


def actualizar_ranking(tiempo: int,
                       vidas:int,
                       nombre_jugador: str)-> None:
    '''
    Actualiza el ranking con la vidas, el tiempo obtenidos y los puntos obtenidos junto con el nombre del jugador.
    
    PARAMETROS: "tiempo" -> tiempo obtenido en el nonograma.
                "vidas" -> vidas obtenidas en el nonograma.
                "nombre_jugador" -> nombre del jugador.
    '''
    ranking = convertir_csv_matriz("archivos/ranking.csv")
    puntuacion = calcular_puntuacion(tiempo, vidas)
    minutos, segundos = formatear_tiempo(tiempo)
    tiempo_formateado = f"{minutos}:{segundos}"
    ranking.append([nombre_jugador, tiempo_formateado, vidas, puntuacion])
    ranking_ordenado = ordenar_ranking(ranking)
    escribir_csv("archivos/ranking.csv", ranking_ordenado, ["Nombre", "Tiempo", "Vidas", "Puntuacion"])


def crear_matriz(filas: int,
                 columnas: int,
                 valor = False)->list:
    '''
    Descripción: Genera una nueva matriz de las dimensiones especificadas, inicializando cada celda con el valor dado.

    Parámetros: filas : Un entero que determina la cantidad de sub-listas que contendrá la lista principal (la dimensión vertical).

                columnas : Un entero que define cuántos elementos tendrá cada sub-lista (la dimensión horizontal).

                valor : El dato inicial (puede ser int, None, bool, etc.) que se replicará en cada una de las posiciones de la estructura generada.

    Retorno: La matriz creada.
    '''

    matriz= []
    for _ in range(filas):
        fila_creada = [valor] * columnas
        matriz += [fila_creada]
    
    return matriz


def convertir_csv_matriz(ruta: str)-> list:
    '''
    Convierte el archivo csv a una matriz.
    
    Parametros: ruta ->  Una cadena de texto con la dirección relativa o absoluta del archivo en disco. La función utiliza esto para abrir el flujo de lectura del archivo.

    Retorno: La matriz con el contenido del archivo.
    '''
    with open(ruta) as archivo:
        matriz = []

        for linea in archivo:
            linea = linea.rstrip("\n")
            fila = []
            valores = linea.split(",")

            for valor in valores:
                if valor.isdigit():
                    fila.append(int(valor))
                else:
                    fila.append(valor)
            
            matriz.append(fila)
    
    return matriz


def extraer_columna(matriz: list,
                    columna: int)-> list:
    '''
    Pasa las columnas de la matriz a una lista.
    
    Parametros: matriz -> La estructura de datos origen de la cual se obtendrán los datos.

                columna -> El índice numérico que indica la posición fija a leer dentro de cada sub-lista de la matriz.

    Retorno: el valor de la columna como una fila
    '''
    lista = []
    for i in range(len(matriz)):
            lista.append(matriz[i][columna])
    return lista


def escribir_csv(ruta: str,
                 matriz: list,
                 columnas: list)-> None:
    '''
    Escribe el contenido al archivo csv.

    PARAMETROS: "ruta" -> ruta del archivo .csv
                "matriz" -> matriz que contiene los elementos a agregar.
                "columnas" -> columnas del archivo csv. Por ejemplo: ["Nombre", "Tiempo", "Vidas", "Puntuacion"]
    '''
    linea = ""
    with open(ruta, "w", encoding="utf-8") as archivo:
        archivo.write(",".join(columnas) + "\n")
        
        for fila in matriz:
            linea = ""
            for i in range(len(fila)):

                linea += str(fila[i])

                if i < (len(fila)-1):
                    linea += ","
        
            archivo.write(linea + "\n")
