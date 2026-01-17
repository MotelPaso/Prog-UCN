
import numpy as np

def buscarAgregar(lista, elemento): 
    if not elemento in lista:
        lista.append(elemento)
    return lista.index(elemento)

def encontrarMaximo(lista):
    maximo = -1
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            indice = i
    return maximo, indice

arch = open('taxis.txt','r', encoding='utf-8')
linea = arch.readline().strip()
matriz = np.zeros([10,6])

maquinas = []
nombres = []
kilometros = []

while linea != "":
    partes = linea.split(';')
    nombre = partes[0]
    maquina = partes[1]
    kilometraje = int(partes[2])

    fila = buscarAgregar(maquinas, maquina) # filas
    columna = buscarAgregar(nombres, nombre) # columnas
    matriz[fila][columna] += kilometraje
    linea = arch.readline().strip()

sumaConductor = []
sumaMaquina = []

for col in range(len(nombres)): # revision por columna
    suma = 0
    for fila in range(len(maquinas)): # revision por fila
        suma += float(matriz[fila][col])
    sumaConductor.append(suma)

maximoLocal = 0

for fila in range(len(maquinas)): # revision por fila
    suma = 0
    for col in range(len(nombres)): # revision por columna
        if float(matriz[fila][col]) > maximoLocal: # encontrar maximo
            maximoLocal = float(matriz[fila][col])
            i = fila
            j = col
        suma += float(matriz[fila][col])
    print(f'{maquinas[fila]}, {suma}') # TODO: ordenar lista
    sumaMaquina.append(suma)

ConductorMaximo, indiceConductor = encontrarMaximo(sumaConductor)

maquinaMaxima, indiceMaquina = encontrarMaximo(sumaMaquina)

print(f'{nombres[indiceConductor]}')
print(f'{maquinas[indiceMaquina]}')
print(f'{maximoLocal}, {nombres[j]}, {maquinas[i]}')

