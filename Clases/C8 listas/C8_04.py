"""
7:18, 01/05
"""

def maximoMinimo(a):
    maximo = -1
    minimo = 99999999
    for i in a:
        if i > maximo:
            maximo = i
        if i < minimo:
            minimo = i
    return maximo, minimo

def promedio(a):
    suma = 0
    for i in a:
        suma += i
        promedio = suma/len(a)
    return promedio, suma
    
lista = []
arch = open('numeros.txt','r',encoding= 'utf-8')
linea = arch.readline().strip()
while linea != '':

    numero = int(linea)
    lista.append(numero)
    linea = arch.readline().strip()

maximo, minimo = maximoMinimo(lista)
print(maximo,minimo)










