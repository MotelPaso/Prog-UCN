
# desafio 04

def crear_tablero(longitud,letra):
    lista = []
    for i in range(longitud):
        if i == 0:
            lista.append(letra)
        else:
            lista.append('_')
    return lista

def Movimiento(lista,ficha,letra,contador):
    posicion = lista.index(letra)
    if ficha == letra.upper() and posicion+1 < len(lista): # letra mayuscula
        lista[posicion], lista[posicion+1] = '_', letra
        contador += 1 # cuantas veces ha avanzado
    elif ficha == letra.lower() and posicion != 0: # letra minuscula, si la posicion es inicial no se mueve
        lista[posicion], lista[posicion-1] = '_', letra
    posicion = lista.index(letra) 
    return lista, contador, posicion
    # contador = cuantas veces salio mayuscula
    # posicion = lugar en la carrera

def imprimir_listas(lista,letra):
    print(letra,lista) # imprimo las listas

def encontrar_ganador(posiciones,letras,numeroCarrera):
    ganadores = []
    maximo = -1
    for i in range(len(posiciones)): # me da un maximo para comparar el resto
        if posiciones[i] > maximo:
            maximo = posiciones[i]
            indiceMaximo = i

    for i in range(len(posiciones)): # si son iguales al maximo, son ganadores
        if posiciones[i] == maximo:
            indiceMaximo = i
            ganadores.append(letras[indiceMaximo]) # los añadimos a la lista de ganadores, pero solo sus letras

    if len(ganadores) != 1: # imprimimos el final de las carreras
        salida = str(f'Empate en la carrera {numeroCarrera} entre los robots: ')
        for i in range(len(ganadores)):
            salida += ganadores[i]
            if i != len(ganadores)-1:
                salida += ', '
        print(salida)
    else:
        salida = f"Ganador de la carrera {numeroCarrera}: Robot {ganadores[0]}"
        print(salida)
    return ganadores, maximo

def ordenar_resultados(letras,resultados): 
    resultadosTotales = ['','','','']
    listaLetras = letras
    for i in range(len(resultados)-1): 
        for j in range(i+1,len(resultados)):
            if resultados[i] < resultados[j]:
                resultados[i], resultados[j] = resultados[j], resultados[i]
                listaLetras[i], listaLetras[j] = listaLetras[j], listaLetras[i]
    for i in range(len(resultados)): # añadimos cada resultado a una lista
        resultadosTotales[i] += f'{listaLetras[i]}: {resultados[i]}'
    # la lista queda asi [letra: numero, letra: numero, etc] ya ordenado
    # oye que aqui podria usar un diccionario, pero no dejan usarlo
    return resultadosTotales

def imprimir_resultados(contadores,victorias): 
    print(f'Resultados finales:\n') # el \n sirve para imprimir una nueva linea, podria ser reemplazador por un print("")
    print('Frecuencia de fichas (mayúsculas):')
    for i in contadores: # usando las listas de letras y contadores
        print(i) # imprimimos cada dato de la lista
    print('')
    print('Victorias por robot:')
    for i in victorias: # usando las listas de letras y contadores
        print(i)

arch = open('fichas.txt', 'r', encoding='utf-8') # sacamos el archivo
linea = arch.readline().strip()
partes = linea.split(',')

numCarreras = int(partes[0])
longitudTablero = int(partes[1])

letras = ['A','B','C','D'] # lista con las letras (muy util)
cantidades = [] # cuantas fichas hay por carrera
fichas = [] # las fichas que se van a revisar por carrera
# 0 = primera carrera
# 1 = segunda carrera, etc

while linea != '': # leer el archivo y ordenar los datos en sus listas
    numeroFichas = arch.readline().strip()
    linea = arch.readline().strip()
    cantidades.append(numeroFichas)
    fichas.append(linea)

cont = [0,0,0,0] # cantidad de veces que sale una ficha ganadora
victorias = [0,0,0,0] # cantidad de veces que gano alguien

for j in range(numCarreras):
    posiciones = [0,0,0,0] # posiciones actuales de la carrera
    print(f'Carrera {j+1}:') # imprimir el numero de carrera
    print('')

    fichasLocales = fichas[j].split(',') # separo las fichas a usar en la carrera actual

    listaA = crear_tablero(longitudTablero,'A') # preparo el tablero
    listaB = crear_tablero(longitudTablero,'B')
    listaC = crear_tablero(longitudTablero,'C')
    listaD = crear_tablero(longitudTablero,'D') 

    print('Estado inicial:') # imprimo el estado actual de la carrera
    imprimir_listas(listaA,'A:')
    imprimir_listas(listaB,'B:')
    imprimir_listas(listaC,'C:')
    imprimir_listas(listaD,'D:')
    print('')
    i = 0
    while i < int(cantidades[j]): # si esto es un for, no se puede cortar sin un break, y no se puede usar break
        print(f'Después de la ficha {fichasLocales[i]}:') # mostramos la ficha actual
        listaA, cont[0], posiciones[0] = Movimiento(listaA,fichasLocales[i],'A',cont[0]) 
        listaB, cont[1], posiciones[1] = Movimiento(listaB,fichasLocales[i],'B',cont[1])
        listaC, cont[2], posiciones[2] = Movimiento(listaC,fichasLocales[i],'C',cont[2])
        listaD, cont[3], posiciones[3] = Movimiento(listaD,fichasLocales[i],'D',cont[3])
        # imprimimos los cambios
        imprimir_listas(listaA,'A:')
        imprimir_listas(listaB,'B:')
        imprimir_listas(listaC,'C:')
        imprimir_listas(listaD,'D:')
        print('')
        
        if longitudTablero-1 in posiciones: # para cortar el while
            i = int(cantidades[j])
        i += 1 # tenia que seguir usando el i para no tener que reescribir todo

    ganadores, maximo = encontrar_ganador(posiciones,letras,j+1) # encuentro quien gano y lo imprimo
    
    if maximo != 0:
        for i in range(len(letras)): # contar cuantas veces gano alguien
            if letras[i] in ganadores:
                victorias[i] += 1 
    print('')

contFinal = ordenar_resultados(letras,cont) # ordeno los resultados
victFinal = ordenar_resultados(letras,victorias)
imprimir_resultados(contFinal,victFinal) # mostrar los resultados finales que piden
