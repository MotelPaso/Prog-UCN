
"""
Desafio 5
Teniendo un archivo de texto, revisar el camino recorrido un camion que deja y recibe carga.
"""

import numpy as np
from math import sin,cos

# Ordenar datos del archivo txt
def crear_paises(linea,arch):
    linea = arch.readline().strip()
    paises = []
    paises1 = [] # despues ordeno la lista paises y la necesitaba para algo mas
    while 'Fin' not in linea:
        partes = linea.split(':')
        paises.append(partes[1])
        paises1.append(partes[1])
        linea = arch.readline().strip()
    return paises, paises1

def crear_matriz_normal(linea,arch):
    linea = arch.readline().strip()
    matriz = np.zeros(formaMatriz)
    fila = 0
    while 'Fin' not in linea:
        partes = linea.split(',')
        for colm in range(formaMatriz[1]):
            matriz[fila][colm] = partes[colm]
        fila += 1
        linea = arch.readline().strip()
    return matriz

def crear_tarifas(linea,arch,listaPaises):
    tarifas = np.zeros([len(listaPaises), len(listaPaises)])
    linea = arch.readline().strip()
    while 'Fin' not in linea:
        partes = linea.split(',')
        X = listaPaises.index(partes[0])
        Y = listaPaises.index(partes[1])
        costo = int(partes[2])
        tarifas[X][Y] = costo
        tarifas[Y][X] = costo
        linea = arch.readline().strip()
    return tarifas

def obtener_viajes(linea,arch):
    viajes = []
    cargas = []
    cantMov = []
    mov = []
    while linea != "":
        partes = linea.split(',')
        viajes.append(partes[0])
        cargas.append(float(partes[1]))
        cantMov.append(int(partes[2]))
        lista = []
        for i in range(int(partes[2])):
            linea = arch.readline().strip()
            lista.append(linea)
        mov.append(lista)
        linea = arch.readline().strip()
    return viajes, cargas, cantMov, mov
# Datos acerca del movimiento del camion
def mover_camion(fila,columna,mov):
    if mov == 'Derecha' and columna < formaMatriz[1]-1:
        columna += 1
    if mov == 'Izquierda' and columna >= 0:
        columna -= 1
    if mov == 'Abajo' and fila < formaMatriz[0]:
        fila += 1
    if mov == 'Arriba' and fila > 0:
        fila -= 1
    return fila, columna

def encontrar_terreno(fila,columna):
    return float(terreno[fila][columna])

def revisar_clima(fila,columna,tiempo):
    return max(0, sin(fila)*cos(columna) +tiempo)

def calcular_combustible(terreno,lluvia,carga):
    return carga * (terreno + 0.1) + 5 * lluvia

def ubicar_pais(fila,columna):
    return float(mapa[fila][columna])

def pagar_aduanas(actual,anterior,suma):
    actual -= 1
    anterior -= 1
    if actual != anterior:
        costo = tarifas[int(actual)][int(anterior)]
        print(f'--Aduana de {paises[int(anterior)]} a {paises[int(actual)]}: ${costo}--')
        suma[int(actual)] += 1
    else:
        costo = 0
    return suma, costo
# Impresion de datos relacionados
def puntos3_4_5(tejas,opcion):
    maximo = 0
    for i in range(len(tejas)):
        if tejas[i] > maximo:
            maximo = tejas[i]
            indice = i
    if opcion == 3:
        salida = f'3. País más visitado: {paises[indice]} ({maximo} visitas)'
    elif opcion == 4:
        salida = f'4. País con más carga recibida: {paises[indice]} ({maximo} toneladas)'
    elif opcion == 5:
        salida = f'5. Momento más lluvioso: ({posiciones[indice][0]}, {posiciones[indice][1]}) (t: {indice+1}) - Lluvia: {round(maximo,2)} mm'
    print(salida)
    print(separador)

def calcular_cargas_recibidas(cargas,paisIni,paisFin,carga):
    paisIni -= 1 # 1
    paisFin -= 1
    if paisFin != paisIni:
        cargas[int(paisFin)] += carga
    return cargas

def distribucion_carga(paises):
    contadores = [0,0,0,0]
    cargas = [0,0,0,0]
    suma = 0
    sumaCargas = 0
    for fila in range(formaMatriz[0]):
        for colm in range(formaMatriz[1]):
            if mapa[fila][colm] == 1:
                contadores[0] += 1
                cargas[0] += material[fila][colm]
            elif mapa[fila][colm] == 2:
                contadores[1] += 1
                cargas[1] += material[fila][colm]
            elif mapa[fila][colm] == 3:
                contadores[2] += 1
                cargas[2] += material[fila][colm]
            elif mapa[fila][colm] == 4:
                contadores[3] += 1
                cargas[3] += material[fila][colm]
            suma += 1

    contadores, paises, cargas = ordenar_listas(contadores,paises, cargas)
    promediosMapa = []
    promediosCarga = []
    salida8 = ['8. Distribución del mapa político: ']
    salida9 = ['9. Distribución de carga en países: ']
    for i in range(len(cargas)):
        sumaCargas += cargas[i]
    for i in range(len(paises)):
        promediosMapa.append(contadores[i]*100/suma)
        promediosCarga.append(cargas[i]*100/sumaCargas)
        salida8.append((f'{paises[i]}: {round(promediosMapa[i],2)}%'))
    for i in range(len(paises)):
        salida9.append((f'{paises[i]}: {cargas[i]} toneladas ({round(promediosCarga[i],2)}%)'))
    return salida8, salida9

def ordenar_listas(lista1,lista2,lista3):
    for i in range(len(lista1)-1):
        for j in range(i+1, len(lista2)):
            if lista1[i] < lista1[j]:
                lista1[i], lista1[j] = lista1[j], lista1[i]
                lista2[i], lista2[j] = lista2[j], lista2[i]
                lista3[i], lista3[j] = lista3[j], lista3[i]
    return lista1, lista2, lista3

def ubicaciones_mayor_carga():
    print('7. Top 5 ubicaciones con mayor carga acumulada:')
    maximo = 0
    maximos = []
    paisMaximo = []
    posiciones = []
    i = 0
    while i < 5:
        maximo = 0
        posicionMax = [0,0]
        for fila in range(formaMatriz[0]):
            for colm in range(formaMatriz[1]):
                if material[fila][colm] > maximo:
                    maximo = float(material[fila][colm])
                    posicionMax = [fila,colm]
                    mapaMax = int(mapa[fila][colm])
        material[posicionMax[0]][posicionMax[1]] = 0
        maximos.append(maximo)
        paisMaximo.append(paises1[mapaMax-1])
        posiciones.append(posicionMax)
        i+=1
    for i in range(len(maximos)):
        X = posiciones[i][0]
        Y = posiciones[i][1]
        print(f'({X}, {Y}): {maximos[i]} toneladas - País: {paisMaximo[i]}')

arch = open('Desafio05.txt', 'r', encoding= 'utf-8')
linea = arch.readline().strip()
partes = linea.split(',')
formaMatriz = [int(partes[0]),int(partes[1])]
separador = '-'*22
linea = arch.readline().strip()

while linea != '': # Reunir datos
    if 'Países' in linea:
        paises,paises1 = crear_paises(linea,arch)
    elif 'Mapa' in linea:
        mapa = crear_matriz_normal(linea,arch) # misma
    elif 'Tarifas' in linea:
        tarifas = crear_tarifas(linea,arch,paises)
    elif 'Terreno' in linea:
        terreno = crear_matriz_normal(linea,arch) # misma
    elif 'Material' in linea:
        material = crear_matriz_normal(linea,arch) # misma
    elif 'Viaje' in linea:
        viajes, cargas, cantMov, mov = obtener_viajes(linea,arch)
    linea = arch.readline().strip()

tiempo = 0
filaActual = (formaMatriz[0]-1)
colmActual = 0
paisActual = ubicar_pais(filaActual,colmActual)
paisAnterior = paisActual
aduanaTotal = 0
visitas = [0,0,0,0]
cargas_recibidas = [0,0,0,0]
costoFinal = 0
lluvias = []
posiciones = []

for viaje in range(len(viajes)): # Simular camino
    carga = cargas[viaje]
    consumoViaje = 0
    aduanaLocal = 0
    paisInicial = paisActual
    material[filaActual][colmActual] -= carga
    print(f'Inicio {viajes[viaje]} - Carga: {carga} ton')

    for movimiento in range(1,cantMov[viaje]+1):
        tiempo += 1

        movActual = mov[viaje][movimiento-1]
        filaActual,colmActual = mover_camion(filaActual,colmActual,movActual)
        # encontrar datos en base a la posicion y tiempo actuales
        terrenoActual = encontrar_terreno(filaActual,colmActual)
        lluviaActual = revisar_clima(filaActual,colmActual,tiempo)
        paisActual = ubicar_pais(filaActual,colmActual)

        visitas, aduana = pagar_aduanas(paisActual,paisAnterior, visitas)
        consumoActual = calcular_combustible(terrenoActual,lluviaActual,carga)
        aduanaLocal += aduana

        print(f'(t: {tiempo}) - {movActual} - ({filaActual}, {colmActual}), Terreno: {terrenoActual}, Lluvia: {round(lluviaActual,2)}, País: {paisActual}, Consumo: {round(consumoActual,2)}')
        
        paisAnterior = paisActual
        consumoViaje += consumoActual
        lluvias.append(lluviaActual)
        posiciones.append([filaActual,colmActual])

    cargaFinal = carga + float(material[filaActual][colmActual])
    material[filaActual][colmActual] += carga
    costoConsumo = consumoViaje * 10
    costoViaje = aduanaLocal + costoConsumo
    print(f'Fin {viajes[viaje]} - Carga acumulada en ubicación final ({filaActual}, {colmActual}): {cargaFinal} ton')
    print(f'Consumo total en el viaje: {round(consumoViaje,2)} litros')
    print(f'Dinero gastado: ${round(costoViaje,2)}     ')
    costoFinal += costoViaje
    paisFinal = paisActual
    cargas_recibidas = calcular_cargas_recibidas(cargas_recibidas,paisInicial,paisFinal,carga)
    aduanaTotal += aduanaLocal
    print(separador)

# Impresion final
print(f'2. Total gastado en aduanas: ${aduanaTotal}')
print(separador)
puntos3_4_5(visitas, 3) 
puntos3_4_5(cargas_recibidas, 4)
puntos3_4_5(lluvias, 5)
print(f'6. Dinero gastado en total: ${round(costoFinal,2)}')
print(separador)
salida8, salida9 = distribucion_carga(paises)
ubicaciones_mayor_carga()
print(separador)
for i in salida8:
    print(i)
print(separador)
for i in salida9:
    print(i)
print(separador)