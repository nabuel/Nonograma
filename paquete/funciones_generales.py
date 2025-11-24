def mostrar_matriz(matriz: list)-> None:
    '''
    Descripción: Imprime en la consola una matriz (lista de listas) formateada, fila por fila.

    Parámetros: matriz (la lista de listas a imprimir).
    '''
    #i es el índice de las filas
    for i in range(len(matriz)):

        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print("")


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


def get_binario(mensaje: str)-> int:
    '''
    Obtiene un número binario.

    Parámetros: mensaje -> El mensaje que se le mostrará al usuario para solicitar el número.
    
    Retorno: El número obtenido.
    '''
    numero = input(mensaje)
    while ord(numero) != 48 or ord(numero) != 49:
        print("Número inválido.")
        numero = input(mensaje)
    
    return int(numero)


def get_int(mensaje: str)-> int:
    '''
    Consigue un número entero positivo.

    Parámetros: mensaje -> El mensaje que se le mostrará al usuario para solicitar el número.
    
    Retorno: el número entero conseguido.
    '''
    numero = input(mensaje)

    while not numero.isdigit():
        print("Se le solicita ingresar número entero positivo.")
        numero = input(mensaje)
    
    return int(numero)


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
