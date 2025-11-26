import pygame
from graficos.config import *
import random


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
    Maneja el click realizado por el jugador, cambiando valores gráficos.
    
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
    puntaje = (vidas * 1000000) // tiempo
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


def calcular_datos_nonograma(dibujo: list)-> tuple:
    '''
    Calcula los datos necesarios para el nonograma.

    PARAMETROS: "rutas" -> lista que contine las rutas de los dibujos.
    
    RETORNO: Los datos obtenidos.
    '''

    medida_casillas = calcular_medida_celda(dibujo,(ANCHO_GRILLA, ALTO_GRILLA))
    
    fuente = pygame.font.Font("tipografia/minecraft_font.ttf", int(medida_casillas[0]//2))

    pistas_fila = calcular_pistas_filas(dibujo)

    pistas_columna = calcular_pistas_columna(dibujo)

    longitud_casilla = medida_casillas[0]

    return medida_casillas,fuente,pistas_fila,pistas_columna, longitud_casilla


def calcular_inicio_cuadrado(posicion_click: tuple,
                    aumento: int,
                    coordenada_inicial:tuple)-> tuple:
    '''
    Según donde se clickea se calcula la coordenada de inicio del cuadrado.

    PARAMETROS: "posicion_click" -> coordenada donde se cliqueó.
                "aumento" -> la longitud del cuadrado.
                "coordenda_inicial" -> coordenda donde se inició la grilla.
    
    RETORNO: La coordenada de inicio del cuadrado.
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
        print("Juego terminado. No te quedan vidas.")
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


def formatear_tiempo(milisegundos: int)-> tuple:
    '''
    Convierte el tiempo ingresado en minutos y segundos.
    
    Parametros: "milisegundos" -> milisegundos a convertir en minutos y segundos.
    
    Retorno: Una tupla con minutos, segundos
    
    OBSERVACIÓN: En caso de que sobren milisegundos no se van a retornar.
    '''
    
    segundos_totales = milisegundos // 1000
    
    minutos_retorno = segundos_totales // 60
    segundos_retorno = segundos_totales % 60
    
    return minutos_retorno, segundos_retorno


def obtener_dibujo(lista_rutas: list)-> list:
    '''
    Obtiene un dibujo al azar.
    
    Parametros: "lista_rutas" -> La lista con las rutas de los dibujos.

    Retorno: el dibujo seleccionado
    '''
    numero_dibujo = random.randint(0,len(lista_rutas)-1)
    dibujo = convertir_csv_matriz(lista_rutas[numero_dibujo])

    return dibujo


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


def manejar_caso_correcto(valor_click: int,
                        grilla_jugador: list,
                        posicion_mouse: tuple,
                        longitud_celda: int,
                        lista_coordenadas_espera: list):
    '''
    Aplica los cambios del caso correcto
    '''
    fila,columna = convertir_coordenadas_matriz(posicion_mouse, (X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)
    
    if valor_click == 3:
        grilla_jugador[fila][columna] = 0                                
    else:
        grilla_jugador[fila][columna] = 1

    if posicion_mouse in lista_coordenadas_espera:
        lista_coordenadas_espera.remove((posicion_mouse))


def ejecutar_delay(lista_coordenadas_espera: list,
                   vidas: int,
                   set_coordenadas_correctas: set,
                   set_coordenadas_cruz: set,
                   set_coordenadas_cuadrado: set,
                   grilla_jugador: list,
                   lista_tiempos: list,
                   longitud_celda: int)-> int:
    '''
    Docstring for ejecutar_delay
    
    :param lista_coordenadas_espera: Description
    :type lista_coordenadas_espera: list
    :param vidas: Description
    :type vidas: int
    :param set_coordenadas_correctas: Description
    :type set_coordenadas_correctas: set
    :param set_coordenadas_cruz: Description
    :type set_coordenadas_cruz: set
    :param set_coordenadas_cuadrado: Description
    :type set_coordenadas_cuadrado: set
    :param grilla_jugador: Description
    :type grilla_jugador: list
    '''
    
    
    vidas -= 1
    correccion = lista_coordenadas_espera.pop(0)
    set_coordenadas_correctas.add(correccion)
    fila, columna = convertir_coordenadas_matriz(correccion,(X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)

    if correccion in set_coordenadas_cruz:
        set_coordenadas_cruz.discard(correccion)
        set_coordenadas_cuadrado.add(correccion)
        grilla_jugador[fila][columna] = 1 
    else:
        set_coordenadas_cruz.add(correccion)
        set_coordenadas_cuadrado.discard(correccion)
        grilla_jugador[fila][columna] = 0
                    
    lista_tiempos.pop(0)
    
    return vidas


