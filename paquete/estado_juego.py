from .funciones_logicas import *
from .funciones_graficas import *
from graficos.config import *
import pygame.mixer as mixer

def jugar_nonograma_pygame(superficie: any, 
                            imagen_fondo: any, 
                            dibujo: list,
                            datos: list) -> tuple | int:
    """
    Ejecuta la pantalla de juego usando Pygame.
    
    Parametros:
        "superficie" ->  Objeto de superficie de Pygame donde se renderiza el juego.
        "imagen_fondo" -> Imagen de fondo a mostrar durante el juego.
        "dibujo" -> Lista 2D que representa la solución correcta del nonograma.
        "datos" -> Datos de configuración
    
    Retorno:
        Retorna 1 si el usuario presionó ESCAPE para volver al menú principal.
        Retorna (vidas, tiempo_final) donde:
            - vidas -> Número de vidas restantes cuando terminó el juego.
            - tiempo_final -> Tiempo transcurrido en milisegundos desde el inicio.
    """
    
    activo = True

    #Configuración nonograma.
    medida_casillas, fuente, pistas_fila, pistas_columna, longitud_celda = datos
    vidas = 3

    #Configuración efecto de sonido.
    sonido = mixer.Sound("sonidos/sonido_bloque.mp3")
    sonido.set_volume(0.4)
    sonido_golpe = mixer.Sound("sonidos/sonido_golpe.mp3")
    sonido_golpe.set_volume(0.4)
    
    #Ordenamiento de datos.
    grilla_jugador = crear_matriz(len(dibujo), len(dibujo),None)
    grilla_coordenadas = cargar_coordenadas_grilla(grilla_jugador, longitud_celda,(X_INICIO_GRILLA,Y_INICIO_GRILLA))
    coordenadas_cruz = set()
    coordenadas_cuadrado = set()
    coordenadas_correctas = set()
    estado = None
    lista_coordenadas_espera = []
    lista_tiempos_espera = []
    
    #Configuración del reloj.
    tiempo_inicial = pygame.time.get_ticks()
    tiempo_actual_delay = 0
    inicio_delay = 0
    
    dibujar_cuadrado = dibujar("cuadrado")

    pygame.init()

    while activo:
        cronometro = pygame.time.get_ticks()
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
        
        
            if evento.type == pygame.KEYUP:
                if evento.key ==  pygame.K_ESCAPE:
                    estado = 1
                    activo = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = pygame.mouse.get_pos()
                sonido.play()
                #Si la posición del mouse está dentro de la grilla.
                if validar_click_grilla(posicion_mouse):
                    posicion_mouse = calcular_inicio_cuadrado(posicion_mouse, longitud_celda, (X_INICIO_GRILLA,Y_INICIO_GRILLA))
                    valor_click = evento.button
                    
                    if valor_click == 1 or valor_click == 3:
                        estado = definir_estado_click(posicion_mouse, grilla_jugador, longitud_celda, valor_click, dibujo,coordenadas_correctas)
                        
                        match estado:
                            case "correcto":
                                
                                manejar_click(valor_click, "correcto", coordenadas_correctas, coordenadas_cruz, coordenadas_cuadrado, posicion_mouse)
                                
                                manejar_caso_correcto(valor_click, grilla_jugador, posicion_mouse, longitud_celda, lista_coordenadas_espera)

                                tiempo_actual_delay = 0
                                
                            case "incorrecto":
                                
                                manejar_click(valor_click, "incorrecto", coordenadas_correctas, coordenadas_cruz, coordenadas_cuadrado,posicion_mouse)
                                
                                inicio_delay = pygame.time.get_ticks()
                                
                                if posicion_mouse not in lista_coordenadas_espera:
                                    if posicion_mouse not in coordenadas_correctas:
                                        lista_coordenadas_espera.append(posicion_mouse)
                                        lista_tiempos_espera.append(inicio_delay)

                            case _:
                                pass
                                
        
    
        
        if len(lista_coordenadas_espera) > 0:
            tiempo_actual_delay = pygame.time.get_ticks() - lista_tiempos_espera[0] 
            if tiempo_actual_delay >= DELAY:
                vidas = ejecutar_delay(lista_coordenadas_espera,vidas,coordenadas_correctas,coordenadas_cruz, coordenadas_cuadrado,grilla_jugador,lista_tiempos_espera,longitud_celda)
                sonido_golpe.play()
                tiempo_actual_delay = 0

        
        if vidas == 0:
            activo = False

        if activo != False:
            activo = chequear_final(grilla_jugador, vidas, dibujo)
            tiempo_final = pygame.time.get_ticks() - tiempo_inicial
        
        
        superficie.blit(imagen_fondo, (0,0))
        
        mostrar_corazones(superficie, vidas)
        

        dibujar_cuadrado((ANCHO_GRILLA, ALTO_GRILLA), (X_INICIO_GRILLA, Y_INICIO_GRILLA), BLANCO, superficie)
        
        #Cronómetro que se muestra mientras se juega.
        minutos, segundos = formatear_tiempo(cronometro)
        mostrar_texto_pygame(f"{minutos}:{segundos}", superficie,(30,20), 40,AMARILLO)
        
        #DIBUJA LAS PISTAS.
        mostrar_pistas_filas_pygame(pistas_fila,(X_INICIO_GRILLA -25,Y_INICIO_GRILLA),superficie,fuente, NEGRO,longitud_celda)
        mostrar_pistas_columnas_pygame(pistas_columna,(X_INICIO_GRILLA, Y_INICIO_GRILLA - 25), superficie,fuente,NEGRO,longitud_celda)
        
        
        if len(coordenadas_cuadrado) > 0:
            dibujar_cuadrados_especificos(coordenadas_cuadrado, medida_casillas, AZUL, superficie)
        
        if len(coordenadas_cruz) > 0:
            dibujar_cruces_especificas(coordenadas_cruz, longitud_celda, ROJO, superficie)
        
        
        #DIBUJA LINEAS
        funcion = dibujar("linea vertical")
        dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), longitud_celda,len(dibujo),NEGRO,superficie,funcion)

        funcion = dibujar("linea horizontal")
        dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), longitud_celda,len(dibujo),NEGRO,superficie,funcion,True)
        
        mostrar_texto_pygame("Presione ESCAPE si quiere volver al menu principal.",superficie,(20,700),25, AMARILLO)
        

        
        pygame.display.flip()
        
    if estado == 1:
        return 1
    else:
        return vidas, tiempo_final
    


def mostrar_menu(superficie: any, imagen_fondo: any, nombre_jugador: str)-> int:
    '''
    Muestra el menú principal.
    
    Parametros: "superficie" -> superficie en donde se va a mostrar el menú
                "imagen_fondo" -> imagen de fondo del juego.
                "nombre_jugador" -> nombre del jugador actual.
    
    Retorno: la pantalla a ejecutrar
    '''
    pygame.init()
    activo = True
    superficie.blit(imagen_fondo, (0,0))
    estado = 1
    
    while activo:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RETURN:  # Si el jugador presiona ENTER se inicia el juego.
                    estado = 2
                    activo = False

                elif evento.key == pygame.K_SPACE: # Si el jugador presiona ESPACIO se muestra el ranking
                    estado = 3
                    activo = False

        mostrar_texto_pygame(f"BIENVENIDO {nombre_jugador}", superficie, (10,20),20,AMARILLO)

        #Es el borde negro de las letras
        mostrar_texto_pygame("Presione ENTER para iniciar el juego", superficie, (130,300), 25, NEGRO)
        mostrar_texto_pygame("Presione ESPACIO para ver el ranking", superficie,(130, 370), 25, NEGRO)
        
        mostrar_texto_pygame("Presione ENTER para iniciar el juego", superficie, (130,300), 25, AMARILLO)
        mostrar_texto_pygame("Presione ESPACIO para ver el ranking", superficie,(130, 370), 25, AMARILLO)

        pygame.display.update()

    return estado


def pantalla_ganador_perdedor(superficie: any, imagen_fondo: any, ganador = True) ->int:
    '''
    Muestra la pantalla del ganador y obtiene el nombre de usuario.
    
    PARAMETROS: "superficie" -> superficie en donde se va a mostrar la pantalla de ganador
                "imagen_fondo" -> imagen de fondo del juego.
                "fuente" -> tipografia del texto.
    
    retorno: el nombre del jugador.
    '''
    superficie.blit(imagen_fondo,(0,0))
    sonido_explosion_1 = mixer.Sound("sonidos/explosion_1.mp3")
    sonido_despegue = mixer.Sound("sonidos/despegue_cohete.mp3")
    sonido_explosion_2 = mixer.Sound("sonidos/explosion_2.mp3")
    sonido_explosion_1.set_volume(0.8)
    sonido_despegue.set_volume(0.5)
    sonido_explosion_2.set_volume(0.8)
    
    activo = True

    while activo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                activo = False
            
            if evento.type == pygame.KEYUP:
                if evento.key ==  pygame.K_RETURN:
                        estado = 2
                        return estado

                if evento.key == pygame.K_ESCAPE:
                        estado = 1
                        return estado


        if ganador:
            mostrar_texto_pygame("FELICITACIONES COMPLETASTE EL DIBUJO CORRECTAMENTE!!",superficie,(40,20),20, NEGRO)
            mostrar_texto_pygame("FELICITACIONES COMPLETASTE EL DIBUJO CORRECTAMENTE!!",superficie,(40,20),20, AMARILLO)
            sonido_despegue.play()
            sonido_explosion_1.play()
            sonido_explosion_2.play()
        else:
            mostrar_texto_pygame("TE HAS QUEDADO SIN VIDAS",superficie,(210,20),30, NEGRO)
            mostrar_texto_pygame("TE HAS QUEDADO SIN VIDAS",superficie,(210,20),30, AMARILLO)

        
        mostrar_texto_pygame("Presione ESCAPE si quiere volver al menu principal.",superficie,(20,300),25, NEGRO)
        mostrar_texto_pygame("Presione ENTER si quiere volver a jugar.",superficie,(120,370),25, NEGRO)
        
        mostrar_texto_pygame("Presione ESCAPE si quiere volver al menu principal.",superficie,(20,300),25, AMARILLO)
        mostrar_texto_pygame("Presione ENTER si quiere volver a jugar.",superficie,(120,370),25, AMARILLO)
        

        pygame.display.flip()
    pygame.quit()


def pantalla_ranking(superficie: any,
                     imagen_fondo: any,
                     ruta: str)-> None:
    '''
    Docstring for pantalla_ranking
    
    :param superficie: Description
    :type superficie: any
    :param imagen_fondo: Description
    :type imagen_fondo: any
    :param ruta: Description
    :type ruta: str
    '''
    
    pygame.init()
    activo = True
    superficie.blit(imagen_fondo, (0,0))
    
    while activo:
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                pygame.quit()
            
            if evento.type == pygame.KEYUP:
                if evento.key ==  pygame.K_ESCAPE:
                    estado = 1
                    activo = False

        
        mostrar_texto_pygame("Presione ESCAPE si quiere volver al menu principal.",superficie,(20,50),25, NEGRO)
        mostrar_texto_pygame("Presione ESCAPE si quiere volver al menu principal.",superficie,(20,50),25, AMARILLO)
        
        
        mostrar_ranking(ruta, 10, superficie)

        pygame.display.flip()


    return estado
    