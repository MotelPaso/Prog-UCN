'''
13:52 06/may
'''

def separarLinea(texto,separador):
    division = texto.split(separador)
    return division
# Encontrar el número
def Derecha(texto, buscarPalabra): 
    print('Buscando a la derecha de',buscarPalabra)
    for i in range(len(texto)):
        if texto[i] == buscarPalabra:
            numeroDerecha = texto[i+1]
    print('Encontrado',numeroDerecha)
    return numeroDerecha

def Izquierda(texto, buscarPalabra): 
    print('Buscando a la izquierda de',buscarPalabra)
    for i in range(len(texto)):
        if texto[i] == buscarPalabra:
            numeroIzquierda = texto[i-1]
    print('Encontrado',numeroIzquierda)
    return numeroIzquierda

def Centro(texto):
    print('Buscando centro')
    print('Encontrado', texto[(len(texto)//2)])
    return texto[len(texto)//2]

def Extremos(texto):
    print('Buscando extremos')
    print('Encontrado', texto[0], texto[-1])
    return texto[0], texto[-1]

def Inicio(texto):
    print('Buscando inicio')
    print('Encontrado', texto[0])
    return texto[0]

def Final(texto):
    print('Buscando final')
    print('Encontrado', texto[-1])
    return texto[-1]
# Ver la operacion
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

arch = open("d3.txt", 'r', encoding='utf-8')
linea = arch.readline().strip()
resultado = 0

while linea != "se acabó":
    indices = []
    partes = linea.split(',')
    separador = str(partes[0])
    linea2 = arch.readline().strip() # Revisamos la linea siguiente al mismo tiempo que la primera
    lista = separarLinea(linea2,separador) 

    for i in range(len(partes)): #  Revisar las operaciones
        if i > 1: # Evitar el primer simbolo
            if len(partes[i]) == 1:
                operador = partes[i]
            if partes[i] == 'mayor':
                operador = 'mayor'
            if partes[i] == 'menor':
                operador = 'menor'
        # Revisar que hacer debido a la linea.
        if partes[i] == 'derecha':
            indices.append('derecha')
            palabra = partes[i+1]
            numeroDerecha = Derecha(lista, palabra)
        if partes[i] == 'izquierda':
            indices.append('izquierda')
            palabra = partes[i+1]
            numeroIzquierda = Izquierda(lista, palabra)
        if partes[i] == 'centro':
            indices.append('centro')
            numeroCentro = Centro(lista)
        if partes[i] == 'extremos':
            indices.append('extremos')
            primerNumero,segundoNumero = Extremos(lista)
        if partes[i] == 'inicio':
            indices.append('inicio')
            numeroInicio = Inicio(lista)
        if partes[i] == 'final':
            indices.append('final')
            numeroFinal = Final(lista)
    # NO SE PUEDE HACER DIFERENTE ESTOY LLORANDO
    if indices[0] == 'derecha':
        primerNumero = numeroDerecha
    elif indices[0] == 'izquierda':
        primerNumero = numeroIzquierda
    elif indices[0] == 'centro':
        primerNumero = numeroCentro
    elif indices[0] == 'inicio':
        primerNumero = numeroInicio
    elif indices[0] == 'final':
        primerNumero = numeroFinal
    # Si son dos cosas:
    if len(indices) > 1: 
        if indices[1] == 'derecha':
            segundoNumero = numeroDerecha
        elif indices[1] == 'izquierda':
            segundoNumero = numeroIzquierda
        elif indices[1] == 'centro':
            segundoNumero = numeroCentro
        elif indices[1] == 'inicio':
            segundoNumero = numeroInicio
        elif indices[1] == 'final':
            segundoNumero = numeroFinal
    # Resultado final.
    resultado = Operacion(primerNumero,operador,segundoNumero)
    print('Resultado', resultado)
    print('--------------------')
    linea = arch.readline().strip()

