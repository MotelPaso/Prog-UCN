
"""
Created on Wed Apr 16 18:02:40 2025
"""
contador = 0


def partes(linea):
    partes = linea.split(",")  # Division linea jugadores y cantRondas
    P1 = partes[0]
    P2 = partes[1]
    cantRondas = int(partes[2])
    return P1, P2, cantRondas

def dividir(linea):
    division = linea.split(",")  # Division por Rounds
    numRound = division[0]
    pond = float(division[1])
    cantJuegos = int(division[2])
    return division, numRound, pond, cantJuegos

def pelea(num1, num2, cuenta):
    # ver quien gana el juego
    G1 = False
    G2 = False
    if cuenta[num1] == 'papel' and cuenta[num2] == 'piedra':
        G1 = True
    elif cuenta[num1] == 'piedra' and cuenta[num2] == 'tijera':
        G1 = True
    elif cuenta[num1] == 'tijera' and cuenta[num2] == 'papel':
        G1 = True
    if cuenta[num2] == 'papel' and cuenta[num1] == 'piedra':
        G2 = True
    elif cuenta[num2] == 'piedra' and cuenta[num1] == 'tijera':
        G2 = True
    elif cuenta[num2] == 'tijera' and cuenta[num1] == 'papel':
        G2 = True
    elif cuenta[num1] == cuenta[num2]:
        G1 = False
        G2 = False
    return G1, G2

def ganadorRonda(a, b):
    if a > b:
        print(f"{numRound}: Gana {P1}")
        G1 = True
        G2 = False
    elif b > a:
        print(f"{numRound}: Gana {P2}")
        G1 = False
        G2 = True
    elif a == b:
        print(f"{numRound}: Empate")
        G1 = False
        G2 = False
    return G1, G2

def ganadorJuego(a, b):
    if a > b:
        print(f"Ganador: {P1}")
    elif b > a:
        print(f"Ganador: {P2}")
    elif a == b:
        print("Empate")

arch = open('datos.txt', 'r', encoding="utf-8")
linea = arch.readline().strip()
cantTotal = int(linea)
linea = arch.readline().strip()
while linea != "":  # Leer cada enfrentamiento
    P1, P2, cantRondas = partes(linea)
    print(f'{P1} vs {P2}')
    linea = arch.readline().strip()
    pond1 = 0
    pond2 = 0
    for i in range(cantRondas):  # Ver cada ronda de juego.
        division, numRound, pond, cantJuegos = dividir(linea)
        contWins1 = 0
        contWins2 = 0
        for i in range(0, cantJuegos*2, 2):  # Ver cada juego.
            G1, G2 = pelea(i+3, i+4, division)
            if G1 is True:
                contWins1 += 1
            elif G2 is True:
                contWins2 += 1
        G1, G2 = ganadorRonda(contWins1, contWins2)
        pond1 += int(G1) * pond
        pond2 += int(G2) * pond
        linea = arch.readline().strip()
    ganadorJuego(pond1, pond2)
    contador += 1
    if contador < cantTotal:
        print('-')
