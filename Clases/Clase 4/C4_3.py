"""
Created on Sat Apr  5 16:41:26 2025
Creado para enseñar, intenta optimizarlo utilizando def.
"""

maximo = 0

arch = open("sucursales.txt", "r", encoding = "utf-8")
linea = arch.readline().strip()

while linea != "":
    maxLocal = 0
    edades = 0
    contador = 0
    partes = linea.split(",")
    ciudad = partes[0]
    trabajadores = int(partes[1])
    
    if ciudad == "Antofagasta":

        print("ANTOFA")
        rep = int(partes[1])
        for i in range(rep):
            linea = arch.readline().strip()
            partes = linea.split(",")
            print(partes[0], partes[1])
            edades += int(partes[1])
            if int(partes[1]) > maxLocal:
                maxLocal = int(partes[1])
            if int(partes[1]) >= 25 and int(partes[1]) <= 30:
                contador += 1
        promedio = edades / rep
        print(f"El promedio es: {round(promedio, 1)}")
        print(maxLocal)
        print(contador)
        
    if ciudad == "Calama":

        print("CALAMA")
        rep = int(partes[1])
        for i in range(rep):
            linea = arch.readline().strip()
            partes = linea.split(",")
            print(partes[0], partes[1])
            edades += int(partes[1])
            if int(partes[1]) > maxLocal:
                maxLocal = int(partes[1])
            if int(partes[1]) >= 25 and int(partes[1]) <= 30:
                contador += 1
        promedio = edades / rep
        print(f"El promedio es: {round(promedio, 1)}")
        print(maxLocal)
        print(contador)

    if ciudad == "La Serena":
        print("LA SERENA")
        rep = int(partes[1])
        for i in range(rep):
            linea = arch.readline().strip()
            partes = linea.split(",")
            print(partes[0], partes[1])
            edades += int(partes[1])
            if int(partes[1]) > maxLocal:
                maxLocal = int(partes[1])
        promedio = edades / rep
        print(f"El promedio es: {round(promedio, 1)}")
        print(maxLocal)
    if partes[1] == "33":
        print(partes[0], ciudad)
    if rep > maximo:
        maximo = rep
    if rep == maximo:
        print(f"la ciudad con más trabajadores es: {ciudad}")
    linea = arch.readline().strip()
    