
import numpy as np

def imprimir_aprobacion(nombres,notas):
    aprobado = 0
    reprobado = 0
    nombresReca = []
    notasReca = []
    for i in range(len(notas)):
        if notas[i] < 3.4:
            reprobado += 1
        elif notas[i] >= 4.0:
            aprobado += 1
        else:
            nombresReca.append(nombres[i])
            notasReca.append(notas[i])
    perApro = aprobado*100 / len(notas)
    perRep = reprobado*100 / len(notas)
    print(f'El porcentaje de alumnos reprobados es {perRep}%')
    print('=================================================')
    print(f'El porcentaje de alumnos aprobados es {perApro}%')
    print('=================================================')
    for i in range(len(nombresReca)):
        print(f'{nombresReca[i]} va a recalificacion con nota {notasReca[i]}')

def imprimir_datos(maximo,nombremax,promedio,nombres,notas):
    print('=================================================')
    print(f'La mejor nota de la prueba parcial 1 fue un {maximo} de {nombremax}')
    print('=================================================')
    print(f'El promedio de la prueba parcial 2 fue de {promedio}')
    print('=================================================')
    print('Populares:')
    for i in range(len(nombres)):
        if 'Frana' in nombres[i]:
            print(f'{nombres[i]}: {notas[i]}')
        if 'Ailin' in nombres[i]:
            print(f'{nombres[i]}: {notas[i]}')
        if 'Alexander' in nombres[i]:
            print(f'{nombres[i]}: {notas[i]}')
    print('=================================================')

def imprimir_matriz(matriz,nombres):
    print('Matriz de notas:')
    salida = '               PP1,'
    for i in range(1,11):
        salida += f" C{i},"
    salida += ' PP2'
    print(salida)
    for i in range(len(nombres)):
        listaSalida = '['
        for j in range(12):
            listaSalida += str(matriz[i][j])
            if j != 11:
                listaSalida += ' '
        listaSalida += ']'
        salida = ''
        salida += f'{nombres[i]}: '
        salida += listaSalida
        print(salida)

arch = open("notas.txt",'r',encoding='utf-8')
linea = arch.readline().strip()

nombres = [] # lista de estudiantes
notas = [] # lista de notas por estudiante, con los mismos indices
while linea != "":
    partes = linea.split(': ') # divido los datos en dos listas
    nombres.append(partes[0])
    notas.append(partes[1])
    linea = arch.readline().strip()

matriz = np.zeros([len(nombres),12])

for fila in range(len(nombres)): # hacemos la matriz con las notas
    partes = notas[fila].split(',')
    cantColumnas = 12
    for col in range(cantColumnas):
        matriz[fila][col] = round(float(partes[col]),1)

maxPP1 = 0
sumaPP2 = 0
promedios = []

for fila in range(len(nombres)):

    NotaPP1 = round(float(matriz[fila][0]),1) # maximo pp1
    if NotaPP1 > maxPP1:
        maxPP1 = NotaPP1
        nombremax = nombres[fila]

    NotaPP2 = round(float(matriz[fila][11]),1) # promedio pp2
    sumaPP2 += NotaPP2

    sumaControles = 0 # promedio controles

    for i in range(1,cantColumnas-1): # sumamos cada control
        sumaControles += round(float(matriz[fila][i]),1)

    promedioControles = round(sumaControles/10,1) # como son 10 controles

    promedioFinal = (NotaPP1 * 0.45 + NotaPP2 * 0.55) * 0.70 + promedioControles * 0.30
    
    promedios.append(round(promedioFinal,1)) # le ponemos cada promedio final a la lista promedios

promedioPP2 = sumaPP2 / len(nombres)
# imprimimos los datos
imprimir_aprobacion(nombres,promedios)
imprimir_datos(maxPP1,nombremax, promedioPP2,nombres,promedios)
imprimir_matriz(matriz,nombres)