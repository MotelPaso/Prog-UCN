

def encontrar_promedio(lista):
    suma = 0
    for i in range(1,4):
        puntaje = int(lista[i])
        suma += puntaje
    promedio = suma/3
    return promedio

def sumar_penalizaciones(lista,promedio):
    suma = 0
    for i in range(4,7):
        penalti = int(lista[i])
        suma += penalti
    puntaje = promedio + suma
    return puntaje, suma

def ordenar_listas(tejas1,tejas2,tejas3):
    for i in range(len(tejas1)-1):
        for j in range(i+1, len(tejas1)):
            if tejas1[i] > tejas1[j]:
                tejas1[i],tejas1[j] = tejas1[j],tejas1[i]
                tejas2[i],tejas2[j] = tejas2[j],tejas2[i]
                tejas3[i],tejas3[j] = tejas3[j],tejas3[i]
    return tejas1, tejas2, tejas3

def imprimir_ganadores(tejas1,tejas2,tejas3):
    for i in range(0,3):
        print(f'El lugar {i+1} fue para {tejas1[i]} con {tejas2[i]} ({tejas3[i]} penalizaciones)' )

arch = open('ejercicio3.txt','r',encoding='utf-8')
linea = arch.readline().strip()
competidores = []
puntajes = []
penaltis = []
while linea != '': # obtener datos y separar en listas
    partes = linea.split(',')

    promedio = encontrar_promedio(partes)
    puntaje, penalizaciones = sumar_penalizaciones(partes,promedio)

    penaltis.append(penalizaciones)
    competidores.append(partes[0])
    puntajes.append(puntaje)
    linea = arch.readline().strip()

puntajes,competidores,penaltis = ordenar_listas(puntajes,competidores,penaltis)
print(competidores)
print(puntajes)
imprimir_ganadores(competidores,puntajes,penaltis)
