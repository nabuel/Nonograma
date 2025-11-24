from .calculos import *
from .funciones_especificas import *
from .funciones_generales import *


def jugar_nonograma_pygame(superficie: any, imagen_fondo: any)-> tuple:
    '''
    Ejecuta el juego del nonograma utilizando Pygame.
    
    Parametros: "superficie" -> 
    
    Retorno: si ganó o perdió el jugador. Y la puntuación obtenida.
    '''
    pygame.init()
    activo = True


    #Configuración nonograma.
    rutas = ["archivos/auto.csv","archivos/buho.csv","archivos/cara_feliz.csv","archivos/gato.csv","archivos/inodoro.csv","archivos/hongo_malo.csv"]
    datos = calcular_datos_nonograma(rutas)
    DIBUJO_CORRECTO = datos[0]
    longitud_celda = datos[5]
    vidas = 3

    #Ordenamiento de datos.
    grilla_jugador = crear_matriz(len(DIBUJO_CORRECTO), len(DIBUJO_CORRECTO),None)
    grilla_coordenadas = cargar_coordenadas_grilla(grilla_jugador, longitud_celda,(X_INICIO_GRILLA,Y_INICIO_GRILLA))
    lista_coordenadas_cruz = set()
    lista_coordenadas_cuadrado = set()
    coordenadas_correctas = set()
    estado = None
    nombre_jugador = ""

    
    #Configuración del reloj.
    tiempo_inicial = pygame.time.get_ticks()



    dibujar_cuadrado = dibujar("cuadrado")
    fila_columna_error_actual = None


    while activo:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                print("Se tocó cerrar")
                activo = False
            
            if evento.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = pygame.mouse.get_pos()

                #Si la posición del mouse está dentro de la grilla.
                
                if validar_click_grilla(posicion_mouse):
                    posicion_mouse = calcular_inicio_cuadrado(posicion_mouse, longitud_celda, (X_INICIO_GRILLA,Y_INICIO_GRILLA))
                    valor_click = evento.button
                    if valor_click == 1 or valor_click == 3:
                        estado = definir_estado_click(posicion_mouse, grilla_jugador, longitud_celda, valor_click, DIBUJO_CORRECTO,coordenadas_correctas)
                        
                        match estado:
                            case "correcto":
                                datos_click = manejar_click(valor_click, "correcto", coordenadas_correctas, lista_coordenadas_cruz, lista_coordenadas_cuadrado, posicion_mouse)
                                fila,columna = convertir_coordenadas_matriz(posicion_mouse, (X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)
                                
                                if valor_click == 1:
                                    grilla_jugador[fila][columna] = 1
                                elif valor_click == 3:
                                    grilla_jugador[fila][columna] = 0
                                

                                if fila_columna_error_actual != None:
                                    fila,columna = fila_columna_error_actual

                                
                            case "incorrecto":
                                datos_click = manejar_click(valor_click, "incorrecto", coordenadas_correctas, lista_coordenadas_cruz, lista_coordenadas_cuadrado,posicion_mouse)
                                
                                print(lista_coordenadas_cruz)
                                print(lista_coordenadas_cuadrado)
                                
                                fila, columna = convertir_coordenadas_matriz(posicion_mouse, (X_INICIO_GRILLA,Y_INICIO_GRILLA),longitud_celda,grilla_jugador)
                                grilla_jugador = pintar_casilla(grilla_jugador, (fila,columna),invertir_cuadrado(valor_click))
                                if posicion_mouse not in coordenadas_correctas:
                                    vidas -= 1
                                    grilla_jugador = pintar_casilla(grilla_jugador, (fila,columna),invertir_cuadrado(valor_click))
                                    lista_coordenadas_cruz, lista_coordenadas_cuadrado = arreglar_coordenadas_pygame(valor_click, posicion_mouse,lista_coordenadas_cruz,lista_coordenadas_cuadrado)
                                    print(f"Casilla incorrecta. Pierdes una vida. Vidas restantes: {vidas}")
                                print("-------------------------------")
                                print(lista_coordenadas_cruz)
                                print(lista_coordenadas_cuadrado)
                                
                                print(f"No se puede marcar una casillas ")

                            case _:
                                pass
                                

            
       

        
        superficie.blit(imagen_fondo, (0,0))
        dibujar_cuadrado((ANCHO_GRILLA, ALTO_GRILLA), (X_INICIO_GRILLA, Y_INICIO_GRILLA), BLANCO, superficie)
        
        
        mostrar_pistas_filas_pygame(datos[3],(X_INICIO_GRILLA -25,Y_INICIO_GRILLA),superficie,datos[2], NEGRO,datos[5])
        #DIBUJA LAS PISTAS DE LAS COLUMNAS.
        mostrar_pistas_columnas_pygame(datos[4],(X_INICIO_GRILLA, Y_INICIO_GRILLA - 25), superficie,datos[2],NEGRO,datos[5])

        
        if len(lista_coordenadas_cuadrado) > 0:
            dibujar_cuadrados_especificos(lista_coordenadas_cuadrado, datos[1], AZUL, superficie)
        
        if len(lista_coordenadas_cruz) > 0:
            dibujar_cruces_especificas(lista_coordenadas_cruz, datos[5], ROJO, superficie)
        
        #DIBUJA LINEAS
        funcion = dibujar("linea vertical")
        dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,superficie,funcion)

        funcion = dibujar("linea horizontal")
        dibujar_lineas((X_INICIO_GRILLA,Y_INICIO_GRILLA), datos[5],len(datos[0]),NEGRO,superficie,funcion,True)
        
        
        if activo != False:
            activo = chequear_final(grilla_jugador, vidas, DIBUJO_CORRECTO)
            if activo == False and vidas > 0:
                    while nombre_jugador == "":
                        nombre_jugador = obtener_texto_pygame("Ingrese su nombre: ", superficie,imagen_fondo, datos[2])
            tiempo_final = pygame.time.get_ticks() - tiempo_inicial
        
        
        #Cronómetro que se muestra mientras se juega.
        cronometro = pygame.time.get_ticks()
        minutos, segundos = formatear_tiempo(cronometro)
        mostrar_texto_pygame(f"{minutos}:{segundos}", superficie,(0,0), 70)
    
        pygame.display.update()

    
    return vidas, tiempo_final, nombre_jugador



def mostrar_menu(superficie: any, imagen_fondo: any)-> None:
    '''
    Muestra el menú principal.
    
    Parametros: "superficie" -> superficie en donde se va a mostrar el menú
                "icono" -> icono del juego.
                "imagen_fondo" -> imagen de fondo del juego.
    '''
    pygame.init()
    activo = True
    superficie.blit(imagen_fondo, (0,0))
    
    while activo:

        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                print("Se tocó cerrar")
                pygame.quit()
            
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RETURN:  # Si el jugador aprieta enter se inicia el juego.
                    estado = 2
                    activo = False
                    print("Se ejecutará el juego")
                elif evento.key == pygame.K_SPACE:
                    estado = 3
                    activo = False
                    print("Se mostrará el ranking")

        
        mostrar_texto_pygame("Presione ENTER para iniciar el juego", superficie, (210,300), 30)
        mostrar_texto_pygame("Presione ESPACIO para ver el ranking", superficie,(210, 350), 30)

        pygame.display.update()

    return estado
