from .validaciones import *
from .funciones_generales import *
from .calculos import *
import pygame


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
    
    Parametros: "inicio"-> Punto de inicio de la linea.
                "aumento"-> es el valor por el cual el eje x irá aumentando.
                "repeticiones" -> la cantidad de veces que se ejecutará el proceso.
                "color" -> color de la linea.   
                "superficie"-> la superficie donde será pintada las lineas.
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
                     superficie: any)-> None:
    '''
    Dibuja un cuadrado en la posición indicada con Pygame.
    
    Parámetros: "medidas"-> Son las medidas del cuadrado por ejemplo (40,40)
                "coordenada_inicio" -> es la coordenada de la punta superior izquierda del cuadrado.
                "color" -> color del cuadrado.
                "superficie"-> la superficie donde será pintado el cuadrado.
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
    x,y = coordenada_inicio

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
                "color" -> color del cuadrado.
                "superficie" -> la superficie donde será pintado el cuadrado.
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


def mostrar_pistas_filas_pygame(lista_pistas: tuple,
                        coordenadas: tuple,
                        superficie: any,
                        fuente: int|float,
                        color: tuple,
                        aumento: int)-> None:
    '''
    Muestra las pistas de las filas en Pygame.
    
    PARAMETROS: "lista_pistas" -> es una lista que contiene las pistas de las filas.
                "coordenadas" -> coordenada donde se empezarán a dibujar las pistas.
                "superficie" -> la superficie donde será pintado el cuadrado.
                "fuente" -> fuente para escribir las pistas.
                "color" -> color de las pistas.
                "aumento" -> es el valor por el cual los ejes irán aumentado.
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
    Muestra las pistas de las columnas en Pygame.
    
    Parametros: "lista_pistas" -> es una lista que contiene las pistas de las columnas.
                "coordenadas" -> coordenada donde se empezarán a dibujar las pistas.
                "superficie" -> la superficie donde será pintado el cuadrado.
                "fuente" -> fuente para escribir las pistas.
                "color" -> color de las pistas.
                "aumento" -> es el valor por el cual los ejes irán aumentado.
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


def mostrar_ranking(ruta: str,
                    limite: int)-> None:
    '''
    Muestra los primeros 10 jugadores del ranking.
    
    Parametros: "ruta" -> ruta del archivo csv donde se encuentra el ranking.
                "limite" -> límite de jugadores a mostrar.
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
                "longitud_cruz"-> longitud de la cruz.
                "superficie"-> la superficie donde será pintado la cruz.
    '''
    x,y = inicio
    
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


def obtener_texto_pygame(mensaje: str, superficie: any, imagen_fondo: any, fuente: any)-> str:
    '''
    Obtiene un texto utilizando Pygame.
    
    Parametros: mensaje -> El mensaje que se le mostrará al usuario para solicitar el texto.
    
    Retorno: El texto obtenido.
    '''
    texto_ingresado = ""
    texto_ingresado_rect = pygame.Rect(X_INICIO_GRILLA, Y_INICIO_GRILLA, 200, 200)
    activo = True
    pygame.init()
    superficie.blit(imagen_fondo,(0,0))
    dibujar_cuadrado_pygame((300,300),(X_INICIO_GRILLA,Y_INICIO_GRILLA),GRIS, superficie)
    
    while activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    #Borra el último caracter.
                    texto_ingresado = texto_ingresado[0:-1]
                    
                elif evento.key == pygame.K_RETURN:
                    activo = False
                    
                else:
                    texto_ingresado += evento.unicode

        
        mostrar_texto_pygame(mensaje,superficie,(X_INICIO_GRILLA,Y_INICIO_GRILLA),70)
        pygame.draw.rect(superficie,ROJO,texto_ingresado_rect,2)
        
        superficie_texto = fuente.render(texto_ingresado, True, NEGRO)
        
        superficie.blit(superficie_texto, 
                        (texto_ingresado_rect.x,
                        texto_ingresado_rect.y))
        
        pygame.display.flip()
        
    return texto_ingresado 


def mostrar_texto_pygame(texto: str,
                        superficie: any,
                        coordenadas_inicio: tuple,
                        ancho: int)->None:
    '''
    Muestra el texto en pygame.
    
    PARAMETROS: "texto" -> texto a mostrar.
                "superficie" -> ventana en la cual se muestra el texto.
                "coordenadas_inicio" -> ubicación donde se muestra el texto.
                "ancho" -> que tan grande son las letras.
    '''
    fuente = pygame.font.SysFont("Roboto", ancho)
    superficie_texto = fuente.render(texto, True, NEGRO)
    rect_texto = superficie_texto.get_rect()
    
    rect_texto.topleft = coordenadas_inicio
    
    superficie.blit(superficie_texto, rect_texto)
