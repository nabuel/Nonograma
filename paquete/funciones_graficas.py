from .funciones_logicas import *
from graficos.config import *
import pygame


def dibujar_lineas(inicio: tuple,
                    aumento: int,
                    repeticiones: int,
                    color: tuple,
                    superficie: any,
                    funcion: any,
                    sentido= False)->None:
    '''
    Dibuja múltiples líneas en una superficie aplicando una función repetidamente.

    PARAMETROS: "inicio" -> Tupla (x, y) que representa las coordenadas de inicio.
                "aumento" -> valor de incremento para moverse en el eje.
                "repeticiones" -> cantidad de repeticiones para dibujar.
                "color" -> tupla que representa el color (ej. RGB o RGBA).
                "superficie" -> objeto superficie donde se dibujarán las líneas.
                "funcion" -> función callable que dibuja una línea.
                "sentido" -> Si False (default), se mueve en eje x. Si True, en eje y.
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
    Dibuja una linea vertical en Pygame.

    Parametros: "inicio"-> Punto de inicio de la linea.
                "aumento"-> es el valor por el cual el eje y irá aumentando.
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
                "repeticiones" -> cantidad de cuadrados a dibujar.
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
    y = coordenadas[1] - 7
    y = y + dividir(aumento,2)

    for pista in lista_pistas:
        indice = -1
        x = coordenadas[0] - 3
        for i in range(len(pista)):
            texto = fuente.render(str(pista[indice]),True, color)
            if pista[indice] > 9:
                superficie.blit(texto, (x - 7 ,y))
            else:
                superficie.blit(texto, (x,y))
            indice -= 1
            
            x -= dividir(aumento,2) + 3
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

    x = coordenadas[0] - 7
    x = x + dividir(aumento,2) 

    for pista in lista_pistas:
        indice = -1
        y = coordenadas[1] - 10
        for i in range(len(pista)):
            texto = fuente.render(str(pista[indice]),True, color)
            if pista[i] > 9:
                superficie.blit(texto, (x - 5,y))
            else:
                superficie.blit(texto, (x,y))
            indice -= 1
            y -= dividir(aumento,2) + 3
        x += aumento


def mostrar_ranking(ruta: str,
                    limite: int,
                    superficie: any)-> None:
    '''
    Muestra una tabla de ranking en una superficie de Pygame leyendo datos desde un archivo CSV.
    
    PARAMETROS: "ruta" -> ruta del archivo CSV que contiene los datos del ranking.
                "limite" -> cantidad máxima de filas a mostrar desde la matriz de ranking.
                "superficie" -> la superficie donde será pintado el ranking.
    '''
    matriz = convertir_csv_matriz(ruta)
    y = 200

    for i in range(len(matriz)):
        if i > limite:
            break
        x = 150
        for j in range(len(matriz[i])):
            
            texto = matriz[i][j]
            
            if type(texto) != str:
                texto = str(texto)
            
            if len(texto) > 6:
                mostrar_texto_pygame(texto, superficie,(x - 6,y), 20, AMARILLO)
            elif i > 0:
                mostrar_texto_pygame(texto, superficie,(x + 10,y), 20, AMARILLO)
            
            else:
                mostrar_texto_pygame(texto, superficie,(x,y), 20, AMARILLO)
            x += 120
        y += 50


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


def obtener_texto_pygame(superficie: any, fuente: any, imagen_fondo: any)-> str:
    """
    Obtiene un texto ingresado por el usuario utilizando una interfaz gráfica con Pygame.
    
    Parámetros:
        "superficie" -> Superficie de Pygame donde se dibujará la interfaz de entrada de texto.
        "fuente" -> Objeto de fuente de Pygame utilizado para renderizar el texto ingresado.
        "imagen_fondo" -> Imagen de fondo que se mostrará mientras se solicita el texto.
    
    Retorno: El texto ingresado por el usuario.
    """
    
    texto_ingresado = ""
    texto_ingresado_rect = pygame.Rect(X_INICIO_GRILLA, Y_INICIO_GRILLA, 200, 25)
    ancho, alto = superficie.get_size()
    texto_ingresado_rect.center = (ancho // 2, alto // 2)
    activo = True
    pygame.init()

    while activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            
            if evento.type == pygame.KEYUP:
                if evento.key ==  pygame.K_RETURN:
                    if len(texto_ingresado) > 0:
                        texto_ingresado = texto_ingresado[0:-1]
                        return texto_ingresado
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    #Borra el último caracter.
                    if len(texto_ingresado) > 0:
                        texto_ingresado = texto_ingresado[:-1]
                else:
                    if len(texto_ingresado) < 8:
                        texto_ingresado += evento.unicode

        superficie.blit(imagen_fondo,(0,0))
        
        mostrar_texto_pygame("Ingrese un nombre de registro:",superficie,(X_INICIO_GRILLA,Y_INICIO_GRILLA),20, AMARILLO)
        
        superficie_texto = fuente.render(texto_ingresado, True, AMARILLO)
        
        
        superficie.blit(superficie_texto, 
                        (texto_ingresado_rect.x,
                        texto_ingresado_rect.y))
        
        pygame.display.flip()


def mostrar_texto_pygame(texto: str,
                        superficie: any,
                        coordenadas_inicio: tuple,
                        ancho: int,
                        color: tuple)->None:
    '''
    Muestra el texto en pygame.
    
    PARAMETROS: "texto" -> texto a mostrar.
                "superficie" -> ventana en la cual se muestra el texto.
                "coordenadas_inicio" -> ubicación donde se muestra el texto.
                "ancho" -> que tan grande son las letras.
    '''
    fuente = pygame.font.Font("tipografia/minecraft_font.ttf", ancho)
    superficie_texto = fuente.render(texto, True, color)
    rect_texto = superficie_texto.get_rect()
    
    rect_texto.topleft = coordenadas_inicio
    
    superficie.blit(superficie_texto, rect_texto)


def mostrar_corazones(superficie: any, cantidad: int)-> None:
    """
    Dibuja una cantidad específica de corazones ("vidas") en la superficie dada usando Pygame.
    
    Parámetros:
        "superficie" -> Superficie donde se dibujan los corazones.
        "cantidad" ->  Número de corazones a mostrar.
    """
    x = 800
    y = 10
    
    for _ in range(cantidad + 1):
        corazon = crear_vida(x,y,40,40)
        superficie.blit(corazon["surface"], corazon["rect_pos"])
        x -= 50


def crear_vida(x, y, ancho, alto):
    dict_corazon = {}
    dict_corazon["surface"] = pygame.image.load("imagenes/mini_corazon.png")
    dict_corazon["surface"] = pygame.transform.scale(dict_corazon["surface"], (ancho, alto))
    dict_corazon["rect_pos"] = pygame.Rect(x, y, 200, 200)
    dict_corazon["rect"] = pygame.Rect((x+ancho/2) -10, y + 90, 40, 20)

    return dict_corazon