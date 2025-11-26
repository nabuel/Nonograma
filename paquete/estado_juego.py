from .funciones_logicas import *
from .funciones_graficas import *
from graficos.config import *


def jugar_nonograma_pygame(superficie: any, 
                            imagen_fondo: any, 
                            dibujo: list,
                            datos: list)-> tuple | int:
    '''
    Ejecuta el juego del nonograma utilizando Pygame.
    
    Parametros: "superficie" -> 
    
    Retorno: si ganó o perdió el jugador. Y la puntuación obtenida.
    '''
    pygame.init()
    activo = True

    #Configuración nonograma.
    medida_casillas, fuente, pistas_fila, pistas_columna, longitud_celda = datos
    vidas = 3

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
    cronometro = -1
    
    dibujar_cuadrado = dibujar("cuadrado")


    while activo:
        if cronometro == -1:
            cronometro = 0
        
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
        
        
            if evento.type == pygame.KEYUP:
                if evento.key ==  pygame.K_ESCAPE:
                    estado = 1
                    activo = False

            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = pygame.mouse.get_pos()
                
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
                                    lista_coordenadas_espera.append(posicion_mouse)
                                    lista_tiempos_espera.append(inicio_delay)

                            case _:
                                pass
                                
        
        cronometro = pygame.time.get_ticks()
        
        if len(lista_coordenadas_espera) > 0:
            tiempo_actual_delay = pygame.time.get_ticks() - lista_tiempos_espera[0] 
            if tiempo_actual_delay >= DELAY:
                vidas = ejecutar_delay(lista_coordenadas_espera,vidas,coordenadas_correctas,coordenadas_cruz, coordenadas_cuadrado,grilla_jugador,lista_tiempos_espera,longitud_celda)
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
                if evento.key == pygame.K_RETURN:  # Si el jugador aprieta enter se inicia el juego.
                    estado = 2
                    activo = False

                elif evento.key == pygame.K_SPACE:
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
    