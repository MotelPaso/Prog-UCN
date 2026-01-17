

def encontrar_maximos(lista):
    maximos = []
    maximo = 0
    for j in range(3): # encontrar los 3 maximos
        for numero in range(len(lista)):
            lista[numero] = int(lista[numero])
            if lista[numero] > maximo:
                maximo = lista[numero]
                indice = numero
        maximos.append(maximo)
        lista.pop(indice) # no funcionaba con remove
        maximo = 0
    print(maximos)

arch = open('ejercicio1.txt')
linea = arch.readline().strip()
listaNum = []

while linea != '':
    listaNum.append(linea)
    linea = arch.readline().strip()

encontrar_maximos(listaNum)

