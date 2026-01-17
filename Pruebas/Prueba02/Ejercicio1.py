import numpy as np
from matplotlib import pyplot as PLT

def mostrar_imagen(ancho,alto,r,g,b):
    M = np.dstack((r,g,b))
    PLT.imshow(M)
    PLT.show()

def mostrar_menu(opcion):
    print("")
    print("Bienvenido al Editor de Imágenes")
    print("")
    print("C: Cargar imagen")
    print("")
    print("M: Mostrar imagen")
    print("")
    print("B: Aplicar blur")
    print("")
    print("G: Convertir a escala de grises")
    print("")
    print("X: Pixelar")
    print("")
    print("I: Invertir")
    print("")
    print("N: Blanco y negro (normal)")
    print("")
    print("D: Blanco y negro (dither)")
    print("")
    print("S: Salir")
    print("")
    opcion = input(str("Seleccione una opción: ")).upper()
    print("")
    return opcion

def cargar_imagen(archivo):
    arch = open(str(archivo), 'r', encoding='utf-8')
    linea = arch.readline().strip()
    partes = linea.split(' ')

    ancho = int(partes[0])
    alto = int(partes[1])

    imagenR = np.zeros([alto,ancho]) # matrices con r,g,b
    imagenG = np.zeros([alto,ancho])
    imagenB = np.zeros([alto,ancho])
    linea = arch.readline().strip()
    fila = 0

    while linea != '':
        pixeles = linea.split(' ')
        columna = 0
        for i in range(len(pixeles)):
            colores = pixeles[i].split(',')
            rojo = int(colores[0])
            verde = int(colores[1])
            azul = int(colores[2])

            imagenR[fila][columna] = rojo
            imagenG[fila][columna] = verde
            imagenB[fila][columna] = azul
            columna += 1

        fila += 1
        linea = arch.readline().strip()

    return ancho, alto, imagenR, imagenG, imagenB

def aplicar_grises(ancho,alto,r,g,b):
    for fila in range(alto):
        for colm in range(ancho):
            nuevoColor = (0.21*int(r[fila][colm]))+(0.71*int(g[fila][colm]))+(0.07*int(b[fila][colm]))
            r[fila][colm] = nuevoColor
            g[fila][colm] = nuevoColor
            b[fila][colm] = nuevoColor
    return r,g,b

def invertir_colores(ancho,alto,r,g,b):
    for fila in range(alto):
        for colm in range(ancho):
            r[fila][colm] = 255 - r[fila][colm]
            g[fila][colm] = 255 - g[fila][colm]
            b[fila][colm] = 255 - b[fila][colm]
    return r,g,b

def blanco_negro(ancho,alto,r,g,b,dither):
    sumaR = 0
    sumaG = 0
    sumaB = 0
    total = 0
    for fila in range(alto):
        for colm in range(ancho):
            sumaR += int(r[fila][colm])
            sumaG += int(g[fila][colm])
            sumaB += int(b[fila][colm])
            total += 1

    promR = sumaR / total
    promG = sumaG / total
    promB = sumaB / total

    for fila in range(alto-1):
        for colm in range(ancho):
            auxR = int(r[fila][colm]) # para el dither
            auxG = int(g[fila][colm])
            auxB = int(b[fila][colm])

            if r[fila][colm] >= promR: # podria escribirse mejor
                r[fila][colm] = 255
            else:
                r[fila][colm] = 0

            if g[fila][colm] >= promG:
                g[fila][colm] = 255
            else:
                g[fila][colm] = 0

            if b[fila][colm] >= promB:
                b[fila][colm] = 255
            else:
                b[fila][colm] = 0

            if dither is True: # no funciona
                difR = auxR - (r[fila][colm]) 
                difG = auxG - (g[fila][colm]) 
                difB = auxB - (b[fila][colm]) 

                if fila +1 != alto: # abajo
                    r[fila+1][colm] += difR * (5/16) 
                    g[fila+1][colm] += difG * (5/16) 
                    b[fila+1][colm] += difB * (5/16) 
                if colm +1 != ancho: # derecha
                    r[fila][colm+1] += difR * (7/16) 
                    g[fila][colm+1] += difG * (7/16) 
                    b[fila][colm+1] += difB * (7/16)
                if fila +1 != alto and colm-1 >= 0: #abajo,izquierda
                    r[fila+1][colm-1] += difR * (3/16) 
                    g[fila+1][colm-1] += difG * (3/16) 
                    b[fila+1][colm-1] += difB * (3/16) 
                if fila +1 != alto and colm +1 != ancho: #abajo, derecha
                    r[fila+1][colm+1] += difR * (1/16) 
                    g[fila+1][colm+1] += difG * (1/16) 
                    b[fila+1][colm+1] += difB * (1/16)
    return r,g,b

opciones = ['C','M','B','G','X','I','N','D','S']
opcion = ''
cargado = ''

while opcion != "S":
    opcion = mostrar_menu(opcion)
    if opcion == 'C':
        nombreArch = str(input("Ingrese el nombre del archivo: "))
        ancho,alto,r,g,b = cargar_imagen(nombreArch)
        cargado = True
    elif opcion not in opciones:
        print('Opcion no valida.')
    elif opcion != 'S' and not cargado:
        print('Imagen no cargada.')

    if cargado and opcion != 'S':
        if opcion == 'M':
            mostrar_imagen(ancho,alto,r,g,b)
        elif opcion == 'B':
            print('No implementado')
        elif opcion == 'G':
            r,g,b = aplicar_grises(ancho,alto,r,g,b)
        elif opcion == 'X':
            print('No implementado')
        elif opcion == 'I':
            r,g,b = invertir_colores(ancho,alto,r,g,b)
        elif opcion == 'N':
            r,g,b = blanco_negro(ancho,alto,r,g,b,False)
        elif opcion == 'D':
            r,g,b = blanco_negro(ancho,alto,r,g,b,True)
        else:
            print('Opcion no valida.')