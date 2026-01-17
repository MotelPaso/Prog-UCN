# -*- coding: utf-8 -*-

# -------------------- FUNCIONES DEL PROGRAMA --------------------

# Muestra el menú principal y devuelve la opción seleccionada por el usuario
def opcionMenu():
    print('\nOrdenar reportes por')
    print('1) Conductores [A-Z]')
    print('2) Auxiliares [A-Z]')
    print('3) Hora de salida [00-24]')
    print('4) Destinos recurrentes [mayor-menor]')
    print('5) Buscar por patente')
    print('0) Cerrar Programa')
    opcion = input('Seleccione opción: ')
    print('')
    return opcion

# Lee un archivo de texto línea por línea, eliminando saltos de línea y devolviendo una lista de líneas
def leer(txt):
    lista = []
    archivo = open(txt, 'r', encoding='utf-8')  # Abrimos el archivo en modo lectura con codificación UTF-8
    linea = archivo.readline().strip()  # Leemos la primera línea sin saltos de línea
    while linea != '':
        lista.append(linea)  # Agregamos cada línea leída a la lista
        linea = archivo.readline().strip()  # Continuamos leyendo las siguientes líneas
    archivo.close()  # Cerramos el archivo al terminar
    return lista

# Extrae una columna específica de cada línea del archivo como una lista independiente
# lista: lista de líneas del archivo
# indice: número de la columna que se quiere extraer (0=patente, 1=conductor, etc.)
def crearLista(lista, indice):
    nueva_lista = []
    for dato in lista:
        partes = dato.split(',')  # Dividir la línea por comas
        nueva_lista.append(partes[indice])  # Agregar el dato de la columna deseada
    return nueva_lista

# Ordena una lista de manera ascendente (alfabéticamente o numéricamente)
def ordenarMenorMayor(lista):
    for a in range(len(lista) - 1):
        for b in range(a + 1, len(lista)):
            if lista[a] > lista[b]:  # Si el elemento actual es mayor que el siguiente, se intercambian
                aux = lista[a]
                lista[a] = lista[b]
                lista[b] = aux
    return lista

# Encuentra el índice del valor más alto dentro de una lista numérica
# Es el algoritmo de búsqueda mayor, pero retorna su posición en lugar de retornar su valor
def indiceMayor(lista):
    mayor = -1
    for valor in lista:
        if mayor < valor:
            mayor = valor
    return lista.index(mayor)

# Imprime los datos ordenados según el criterio solicitado
# listaOrdenada: lista ordenada por criterio
# listaCompleta: lista con todas las líneas del archivo original
# indice: índice de la columna por la que se ordenó
def imprimir123(listaOrdenada, listaCompleta, indice):
    lista_original = crearLista(listaCompleta, indice)  # Se extrae la columna original

    for dato in listaOrdenada:
        
        posicion = lista_original.index(dato)  # Buscar la posición original del dato
        partes = listaCompleta[posicion].split(',')  # Separar toda la línea por comas
        dato_indice = partes[indice]  # Se extrae el dato clave
        partes.pop(indice)   # Se elimina el dato clave de la lista para evitar duplicación
        salida = dato_indice + ': '  #se crea una valiable tipo string para concatenar los datos en el orden deseado
        for dato in partes:
            salida += dato  #concatena dato en la variable salida
            if dato != partes[-1]:
                salida += ' - '  # Separador visual entre campos es concatenado sólo cuando no el el último elemento
        print(salida)

# Imprime las ciudades de destino ordenadas de mayor a menor según frecuencia
# La variable lista contiene todas las ciudades del archivo
def imprimirDestinos(lista):
    lista_unicos = []       # Lista con ciudades únicas
    cantidad_unicos = []    # Lista con la cantidad de apariciones por ciudad

    for destino in lista:   # Recorre la lista con ciudades
        if destino not in lista_unicos:
            lista_unicos.append(destino)    # Agrega una ciudad a la lista de únicos únicamente si no existe en la lista 
            cantidad_unicos.append(1)       # # Agrega un 1 a la lista de cantidad cada vez que agrega una nueva ciudad
        else:
            posicion = lista_unicos.index(destino)
            cantidad_unicos[posicion] += 1  # Incrementar la frecuencia en caso de que la ciudad ya haya sido agregada a unicos

    # Imprimir las ciudades en orden de mayor a menor frecuencia
    for i in range(len(lista_unicos)):  #Recorre la lista de únicos
        posicion = indiceMayor(cantidad_unicos) #Busca el mayor en la lista de cantidades y guarda su posición
        print(f'{lista_unicos[posicion]}: {cantidad_unicos[posicion]} viajes') #imprime los datos utilizando la posicion
        lista_unicos.pop(posicion)  #elimina el mayor de la lista para que la proxima busqueda del mayor sea el siguiente mayor
        cantidad_unicos.pop(posicion) #elimina el mayor de la lista para que la proxima busqueda del mayor sea el siguiente mayor

# Busca una patente en el cronograma y muestra los datos relacionados
def imprimirPatente(lista_datos, archivo):
    patente = input('Ingresar patente: ').upper()  # Se transforma a mayúsculas por consistencia
    if patente in lista_datos:  #recorre la lista de patentes
        indice = lista_datos.index(patente) # busca la posicion en que se encuentra la patente ingresada
        partes = archivo[indice].split(',')  # Se obtienen todos los campos utilizando el índice
        print(f'Patente {partes[0]} encontrada!')
        print(f'Conductor: {partes[1]}')
        print(f'Auxiliar: {partes[2]}')
        print(f'Hora de salida: {partes[3]}')
        print(f'Ciudad de destino: {partes[4]}')
    else:
        print(f'La patente {patente} no existe')

# -------------------- PROGRAMA PRINCIPAL --------------------

# Se lee el archivo principal con todos los datos del cronograma
archivo = leer('cronograma.txt')
lista_datos = []  # Lista temporal para trabajar según cada opción del menú

# Mensaje inicial
print('SISTEMA DE REPORTES "TERMINAL DE BUSES GENÉRICO 33"')

# Mostrar el menú inicial
opcion = opcionMenu()

# Bucle principal del programa: sigue mostrando el menú hasta que el usuario elija salir
while opcion != '0':
    if opcion == '1':
        print('Conductores por orden alfabético')
        lista_datos = crearLista(archivo, 1)    # Crea una lista sólo con los conductores
        lista_datos = ordenarMenorMayor(lista_datos)    # Ordena alfabéticamente la lista de conductores
        imprimir123(lista_datos, archivo, 1)

    elif opcion == '2':
        print('Auxiliares por orden alfabético')
        lista_datos = crearLista(archivo, 2)    # Crea una lista sólo con los Auxiliares
        lista_datos = ordenarMenorMayor(lista_datos)    # Ordena alfabéticamente la lista de auxiliares
        imprimir123(lista_datos, archivo, 2)

    elif opcion == '3':
        print('Por hora de salida')
        lista_datos = crearLista(archivo, 3)    # Crea una lista sólo con los Horas
        lista_datos = ordenarMenorMayor(lista_datos)    # Ordena alfabéticamente la lista de horas
        imprimir123(lista_datos, archivo, 3)

    elif opcion == '4':
        print('Destinos recurrentes')
        lista_datos = crearLista(archivo, 4)    # Crea una lista sólo con los Ciudades
        imprimirDestinos(lista_datos)

    elif opcion == '5':
        print('Buscar por patente')
        lista_datos = crearLista(archivo, 0)    # Crea una lista sólo con los patentes
        imprimirPatente(lista_datos, archivo)

    else:
        print('Opción Inválida. Intente de nuevo.')

    # Mostrar el menú nuevamente al terminar una opción
    opcion = opcionMenu()

# Mensaje de salida
print('SISTEMA CERRADO')