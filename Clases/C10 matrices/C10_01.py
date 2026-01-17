
import numpy as np

def encontrar_unicos(lista):
    listaUnicos = []
    for i in lista:
        if i not in listaUnicos:
            listaUnicos.append(i)
    return listaUnicos


matriz = np.zeros([6,6])

arch = open('recorridos.txt','r', encoding='utf-8')
linea = arch.readline().strip()

salidas = []
llegadas = []
distancias = []

while linea != "":
    partes = linea.split(",")
    salidas.append(partes[0])
    llegadas.append(partes[1])
    distancias.append(float(partes[2]))
    linea = arch.readline().strip()

ciudades = encontrar_unicos(salidas + llegadas)

for k in range(len(salidas)): # 0,1,2,3,4
    i = ciudades.index(salidas[k]) # 0
    j = ciudades.index(llegadas[k]) # 1
    matriz[i][j] = distancias[k] #0,1
    matriz[j][i] = distancias[k] #1,0

arch.close()
print(matriz)
arch = open("viajes.txt",'r',encoding='utf-8')
linea = arch.readline().strip()
salidasSolicitadas = []
llegadasSolicitadas = []
while linea != "":
    partes = linea.split(",")
    salidasSolicitadas.append(partes[0])
    llegadasSolicitadas.append(partes[1])
    linea = arch.readline().strip()

for k in range(len(salidasSolicitadas)):
    if salidasSolicitadas[k] in ciudades and llegadasSolicitadas[k] in ciudades:
        i = ciudades.index(salidasSolicitadas[k])
        j = ciudades.index(llegadasSolicitadas[k])
        if matriz[i][j] != 0:
            print(f'{salidasSolicitadas[k]} y {llegadasSolicitadas[k]} estan a {matriz[i][j]}km de distancia.')
        else:
            print(f"{salidasSolicitadas[k]} y {llegadasSolicitadas[k]} no estan conectadas.")
    elif salidasSolicitadas[k] not in ciudades:
        print(f"{salidasSolicitadas[k]} no existe.")
    elif llegadasSolicitadas[k] not in ciudades:
        print(f"{llegadasSolicitadas[k]} no existe.")

arch.close()