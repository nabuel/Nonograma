from .validaciones import *
from .calculos import *
from .funciones_logicas import *
import pygame


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


#TO DO: CONVERTIR PARA QUE MUESTRE CON PYGAME
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


def obtener_texto_pygame(superficie: any, fuente: any)-> str:
    '''
    Obtiene un texto utilizando Pygame.
    
    Parametros: mensaje -> El mensaje que se le mostrará al usuario para solicitar el texto.
    
    Retorno: El texto obtenido.
    '''
    texto_ingresado = ""
    texto_ingresado_rect = pygame.Rect(X_INICIO_GRILLA, Y_INICIO_GRILLA, 200, 25)
    ancho, alto = superficie.get_size()
    texto_ingresado_rect.center = (ancho // 2, alto // 2)
    activo = True
    pygame.init()

    while activo:
        for evento in pygame.event.get():
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = pygame.mouse.get_pos()
                print(posicion_mouse)
            
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:
                    #Borra el último caracter.
                    if len(texto_ingresado) > 0:
                        texto_ingresado = texto_ingresado[:-1]
                    
                elif evento.key == pygame.K_RETURN:
                    if len(texto_ingresado) > 0:
                        return texto_ingresado
                else:
                    texto_ingresado += evento.unicode


        dibujar_cuadrado_pygame((400, 200),(210,335),BLANCO, superficie)
        
        pygame.draw.rect(superficie,NEGRO,texto_ingresado_rect,2)
        
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
