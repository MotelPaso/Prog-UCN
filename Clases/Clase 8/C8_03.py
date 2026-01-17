

def Unicos(lista):
    listaUnicos = []
    for i in lista:
        if i not in listaUnicos:
            listaUnicos.append(i)
    return listaUnicos

def Repeticiones(lista,listaUnicos):
    contadores = []
    for i in range(len(listaUnicos)):
        contadores.append(0) # Creamos una lista de contadores pensando en el numero de nombres unicos

    for i in range(len(listaUnicos)): # Por cada nombre unico en el archivo
        nombre = lista[i] # Guardamos un nombre para comparar
        for j in range(i,len(lista)): # Revisamos la lista completa de nombres
            if nombre == lista[j]: # Si el nombre revisado es igual al nombre guardado
                contadores[i] += 1 # Le sumamos uno a su contador
    return contadores # Devolvemos el contador

lista = []
arch = open('nombres.txt', 'r', encoding = 'utf-8')
linea = arch.readline().strip()

while linea != '':
    lista.append(linea)
    linea = arch.readline().strip()

unico1 = Unicos(lista)
print(unico1) # Imprimimos la lista de nombres unicos
print(Repeticiones(lista,unico1)) # Con sus respectivas repeticiones

