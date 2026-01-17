

def separar_unicos(lista):
    unicos = []
    for i in lista:
        if i not in unicos:
            unicos.append(i)
    return unicos

def encontrar_repeticiones(listaTotal,unicos):
    contadores = []
    for i in range(len(unicos)):
        contadores.append(0)
    for i in range(len(unicos)):
        for j in listaTotal:
            if unicos[i] == j:
                contadores[i] += 1
    return contadores

def ordenar_listas(tejas2,tejas1):
    # ordenamos en base a tejas1 (la lista con repeticiones)
    for i in range(len(tejas1)-1):
        for j in range(i+1, len(tejas1)):
            if tejas1[i] < tejas1[j]:
                tejas1[i], tejas1[j] = tejas1[j], tejas1[i]
                tejas2[i], tejas2[j] = tejas2[j], tejas2[i]
    return tejas2, tejas1

def imprimir_datos(tejas1,tejas2):
    for i in range(len(tejas1)):
        print(f'{tejas1[i]} {tejas2[i]}')

arch = open('ejercicio2.txt', 'r', encoding='utf-8')
linea = arch.readline().strip()

datos = []
while linea != '':
    datos.append(linea)
    linea = arch.readline().strip()

unicos = separar_unicos(datos)

repeticiones = encontrar_repeticiones(datos,unicos)
unicos, repeticiones = ordenar_listas(unicos,repeticiones)
imprimir_datos(unicos,repeticiones)
