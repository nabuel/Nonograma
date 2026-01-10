# 🧩 Nonograma - Minecraft Edition

¡Bienvenido al **Nonograma**! Un juego de lógica y puzles desarrollado en Python utilizando la librería **Pygame**. Esta versión cuenta con una estética inspirada en Minecraft, incluyendo sonidos, tipografías y gráficos personalizados para ofrecer una experiencia inmersiva.

## 🎮 Características

* **Múltiples Niveles**: Incluye diversos desafíos como "Auto", "Búho", "Cara Feliz", "Gato", "Hongo Malo" e "Inodoro".
* **Sistema de Vidas**: Cuentas con un número limitado de intentos representados por corazones de Minecraft.
* **Ranking Local**: Al finalizar una partida exitosa, puedes registrar tu nombre y ver los mejores tiempos en la tabla de puntuaciones.
* **Ambiente Inmersivo**: Música de fondo y efectos de sonido (explosiones, bloques y golpes) extraídos directamente del universo Minecraft.
* **Interfaz Dinámica**: Configuración visual que se adapta al tamaño de la cuadrícula seleccionada.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje**: Python.
* **Librería Gráfica**: Pygame (para manejo de eventos, gráficos y sonido).
* **Almacenamiento**: Archivos CSV para niveles y rankings.

## 📂 Estructura del Proyecto

El código está organizado de manera modular para facilitar su comprensión:

* `main.py`: Punto de entrada del juego y manejo del bucle principal.
* `paquete/`: Contiene la lógica central del juego, validaciones y estado.
* `graficos/`: Configuraciones de pantalla, colores y constantes visuales.
* `archivos/`: Puzles definidos en formato CSV y el registro de puntajes.
* `imagenes/` & `sonidos/`: Recursos multimedia (sprites, fondos y efectos de audio).

## ⚙️ Instalación y Ejecución

1. **Requisitos previos**: Asegúrate de tener instalado Python y la librería Pygame.
   ```bash
   pip install pygame
