import pygame
from paquete.funciones_logicas import *
from paquete.funciones_graficas import *
from graficos.config import *
from paquete.estado_juego import *

pygame.init()
activo = True


#Configuración pantalla
ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
fondo_imagen = pygame.image.load("imagenes/fondo_minecraft.png")
ventana.blit(fondo_imagen, (0, 0))
ICONO = pygame.image.load("imagenes/icono_minecraft.png")
pygame.display.set_caption("Nonograma")
pygame.display.set_icon(ICONO)
rutas = ["archivos/auto.csv","archivos/buho.csv","archivos/cara_feliz.csv","archivos/gato.csv","archivos/inodoro.csv","archivos/hongo_malo.csv"]
fuente = pygame.font.Font("tipografia/minecraft_font.ttf", 20)


#Configuración de estados.
MENU = 1
JUEGO = 2
RANKING = 3

nombre_jugador = ""
ejecutar = MENU

while activo:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            activo = False
            ejecutar = 0
        
        if ejecutar == MENU:
            while nombre_jugador == "":
                    nombre_jugador = obtener_texto_pygame(ventana, fuente, fondo_imagen)
            ejecutar = mostrar_menu(ventana, fondo_imagen, nombre_jugador)
            
        elif ejecutar == JUEGO:
            
            dibujo = obtener_dibujo(rutas)
            
            datos = calcular_datos_nonograma(dibujo)
            
            resultado = jugar_nonograma_pygame(ventana,fondo_imagen, dibujo, datos)
            
            if type(resultado) == int:
                ejecutar = resultado
            else:
                vidas, tiempo = resultado
                
                if vidas > 0:
                    actualizar_ranking(tiempo,vidas,nombre_jugador)
                    ejecutar = pantalla_ganador_perdedor(ventana,fondo_imagen)
                else:
                    ejecutar = pantalla_ganador_perdedor(ventana, fondo_imagen, False)
            
            pygame.event.clear()
            
        elif ejecutar == RANKING:
            pantalla_ranking(ventana,fondo_imagen,"archivos/ranking.csv")
            ejecutar = 1
            

    
    pygame.display.update()

pygame.quit()