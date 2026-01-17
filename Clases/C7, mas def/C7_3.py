"""
Created on Mon Apr 28 17:10:46 2025
"""

def areaFigura(figura):

    if figura == 'triangulo' or figura == 'tri': 
        # le puse tri para cuando lo iba probando me demorase menos en escribir los datos.
        base = float(input('base? '))
        altura = float(input('altura? '))
        area = (base * altura)/2

    if figura == 'rectantugulo' or figura == 'rec':
        largo = float(input('largo? '))
        ancho = float(input('ancho? '))
        area = (largo * ancho)

    if figura == 'circulo' or figura == 'cir':
        radio = float(input('radio? '))
        pi = 3.14
        area = radio * pi

    return area

cont = 0
maximo = -1

cantFigura = int(input('Cuantas figuras vas a revisar hoy?'))

while cont != cantFigura:

    figura = str(input('Que tipo de figura es? ')).lower()
    area = areaFigura(figura)

    if area > maximo:
        maximo = area
        figuraMaxima = figura

    cont += 1
print('La figura con el mayor area es:',figuraMaxima,'con area de',maximo)