
def guardarJugadores(arch):
    linea = arch.readline().strip()
    jugadores = []
    while (linea != "FIN JUGADORES"):
        partes = linea.split("|")
        jugadores.append(partes)
        linea = arch.readline().strip()
    return jugadores

def guardarGoles(arch):
    linea = arch.readline().strip()
    goles = []
    while (linea != "FIN GOLES"):
        partes = linea.split(",")
        goles.append(partes)
        linea = arch.readline().strip()
    return goles

def mostrarCantidadPorNacion():
    contadores = [0,0,0]
    nacionalidades = ["Chile", "Argentina", "Perú"]
    for jugador in jugadores:
        for j in range(len(nacionalidades)):
            if (jugador[3] == nacionalidades[j]):
                contadores[j] += 1
    salida = "Cantidad de jugadores por nacionalidad:\n"
    for i in range(len(contadores)):
        salida += f"{nacionalidades[i]}: {contadores[i]}\n"

    return salida

def minutoMasGoles():
    minutos = []
    minutosUnicos = []
    contadores = []
    for gol in goles:
        if gol[1] not in minutos:
            contadores.append(1)
            minutosUnicos.append(gol[1])
        else:
            i = minutosUnicos.index(gol[1])
            contadores[i] += 1
        minutos.append(gol[1])
    minutosUnicos, contadores = sortListas2(minutosUnicos, contadores)
    contadores, minutosUnicos = sortListas(contadores, minutosUnicos)
    salida = "Minutos en los que se hacen más goles:\n"

    for i in range(len(minutosUnicos)):
        salida += f"Minuto {minutosUnicos[i]}: {contadores[i]} goles\n"

    return salida

def sortListas(lista, lista1):
    for i in range(len(lista)):
        for j in range(0, len(lista) - 1 - i):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
    return lista, lista1

def sortListas2(lista, lista1):
    for i in range(len(lista)):
        for j in range(0, len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]
    return lista, lista1

def minutoMasGolesChile():
    chilenos = []
    for jugador in jugadores:
        if jugador[3] == "Chile":
            chilenos.append(jugador[0])

    minutos = []
    minutosUnicos = []
    contadores = []

    for gol in goles:
        if gol[0] in chilenos: # Si el jugador es chileno
            if gol[1] not in minutos:
                contadores.append(1)
                minutosUnicos.append(gol[1])
            else:
                i = minutosUnicos.index(gol[1])
                contadores[i] += 1
            minutos.append(gol[1])
    contadores, minutosUnicos = sortListas(contadores, minutosUnicos)
    salida = f"Minuto en el que los jugadores de nacionalidad chilena hacen más goles: Minuto {minutosUnicos[0]} con {contadores[0]} goles\n"
    return salida

def golesRivalPorNacionalidad():
    nacionalidades = []
    for jugador in jugadores:
        if jugador[3] not in nacionalidades:
            nacionalidades.append(jugador[3])
    rivales = []
    for gol in goles:
        if gol[2] not in rivales:
            rivales.append(gol[2])
    salida = "Goles hechos a cada rival y por nacionalidad:\n"
    for i in range(len(rivales)):
        salida += f"Rival: {rivales[i]}\n"
        contadores = [0,0,0]
        for gol in goles:
            if (gol[2] == rivales[i]): # Si el gol fue al rival actual
                nombre = gol[0]
                nacionalidad = encontrarNacionalidad(nombre)
                indice = nacionalidades.index(nacionalidad)
                contadores[indice] += 1

        for j in range(len(contadores)):
            if (contadores[j] != 0):
                salida += f"- {nacionalidades[j]}: {contadores[j]} goles\n"
        if i != len(rivales)-1:
            salida += "\n"
    return salida

def encontrarNacionalidad(nombre):
    for jugador in jugadores:
        if jugador[0] == nombre:
            return jugador[3]

def golesPorPosicion():
    contadores = [0,0,0,0]
    posiciones = ["Delantero", "Lateral", "Mediocampista", "Arquero"]
    for gol in goles:
        for i in range(len(jugadores)):
            if gol[0] in jugadores[i]:
                contadores[posiciones.index(jugadores[i][1])] += 1

    salida = "Goles por posición de los jugadores:\n"
    for i in range(len(posiciones)):
        salida += f"{posiciones[i]}: {contadores[i]} goles\n"
    return salida

arch = open("sharif3.txt","r",encoding="utf-8")
linea = arch.readline().strip()

while(linea != ""):
    if "FIN" not in linea:
        jugadores = guardarJugadores(arch)
    linea = arch.readline().strip()
    goles = guardarGoles(arch)
    linea = arch.readline().strip()

print(mostrarCantidadPorNacion())
print(minutoMasGoles())
print(minutoMasGolesChile())
print(golesRivalPorNacionalidad())
print(golesPorPosicion())

