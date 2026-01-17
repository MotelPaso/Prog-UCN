
# Desafio opcional.


def Horizontal(lineas, separador, palabra):
    for i in lineas:
        if palabra in i and separador in i:
            partes = i.split(separador)
            indice = partes.index(palabra)
            numero = partes[indice + 1]
    return numero
    
def Vertical(lineas, palabra):

    for i in range(len(lineas)):
        if palabra in lineas[i]:
            numero = int(lineas[i+1])
    return numero

def Operacion(primerNumero, operador, segundoNumero):
    primerNumero = int(primerNumero)
    segundoNumero = int(segundoNumero)
    if operador == '+':
        print('Suma',primerNumero, segundoNumero)
        return primerNumero + segundoNumero
    elif operador == '-':
        print('Resta',primerNumero, segundoNumero)
        return primerNumero - segundoNumero
    elif operador == '*':
        print('Multiplicacion',primerNumero, segundoNumero) # balatro
        return primerNumero * segundoNumero
    elif operador == '/':
        print('Division',primerNumero, segundoNumero)
        return primerNumero / segundoNumero
    elif operador == 'mayor':
        print('Mayor',primerNumero, segundoNumero)
        if primerNumero > segundoNumero:
            return primerNumero
        else:
            return segundoNumero
    elif operador == 'menor':
        print('Menor',primerNumero, segundoNumero)
        if primerNumero < segundoNumero:
            return primerNumero
        else:
            return segundoNumero

def buscarIndices(lista,palabra):
    indicesFin = []
    for i in range(len(lista)):
        if lista[i] == palabra:
            indicesFin.append(i)
    return indicesFin

arch = open('d31.txt','r',encoding='utf-8')
linea = arch.readline().strip()

lineas = []
busquedas = 0

while linea != '':
    lineas.append(linea)
    linea = arch.readline().strip()

listaCorte = buscarIndices(lineas,'FIN')

i = 0
contadorModo = 0

while i != len(lineas):
    
    linea = lineas[i]
    partes = linea.split(',')
    if linea == 'FIN':
        pass
    else:
        if len(partes) == 1:
            operador = linea
        else:
            print(partes)
            separador = partes[0]
            modoBusqueda = partes[1]
            seccion = partes[2]
            palabra = partes[3]
            numeros = []

            if modoBusqueda == 'horizontal':
                numero = Horizontal(lineas,separador,palabra)
                numeros.append(numero)
                print(f'Encontrado {palabra} {numero}')
            if modoBusqueda == 'vertical':
                numero = Vertical(lineas,palabra)
                numeros.append(numero)
                print(f'Encontrado {palabra} {numero}')
        if contadorModo%3 == 0:
            Operacion(numeros[i],numeros[i+1],operador)
        contadorModo += 1
    i += 1