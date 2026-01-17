
"""
Created on Sun Apr 13 10:55:41 2025
"""
print('¡Ganadores del torneo internacional de videojuegos en línea 2025!')
categoriasmayores = "retro","soccer","first person shooter"
categoriasmenores = "battle royale","racing"
contOLD = 0
contS = 0
contFPS = 0
contBR = 0
contR = 0
def division(a): # Segunda division
    partes2 = a.split(";")
    nombre = partes2[0]
    edad = int(partes2[1])
    tipo = partes2[2]
    score = int(partes2[3])
    return nombre,edad,tipo,score


errores = 0
arch = open("DatosTorneo.txt", "r", encoding="utf-8")
linea = arch.readline().strip()

while linea != "":
    nombre_max = ""
    nombre_min = ""
    
    max_edad = 0
    min_edad = 99999999999
    max_score = 0
    min_score = 99999999999
    
    partes = linea.split(",")
    juego = partes[0]
    categoria = partes[1]
    cantidad = int(partes[2])
    
    if categoria == "retro":
        contOLD += 1
    if categoria == "soccer":
        contS += 1
    if categoria == "first person shooter":
        contFPS += 1
    if categoria == "battle royale":
        contBR += 1
    if categoria == "racing":
        contR +=1
    
    for i in range(cantidad):
        
        linea = arch.readline().strip()
        nombre, edad, tipo, score = division(linea)
        if categoria in categoriasmayores: # Calculo de Ganadores
            if score > max_score:
                max_score = score
                ganador = nombre
                
        elif categoria in categoriasmenores:
            if score < min_score:
                min_score = score
                ganador = nombre
        # Calculo de edades
        
        if edad > max_edad:
            if edad > 80:
                errores += 1
            else:
                max_edad = edad
                nombre_max = nombre
        if edad < min_edad:
            if edad < 9:
                errores += 1
            else:
                min_edad = edad
                nombre_min = nombre

    if categoria in categoriasmayores:
        print(f"El ganador del juego {juego} de la categoria {categoria} es: {ganador} con {max_score}{tipo}")
    elif categoria in categoriasmenores:
        print(f"El ganador del juego {juego} de la categoria {categoria} es: {ganador} con {min_score}{tipo}")
    print("El jugador con mayor edad en el juego", juego, "es", nombre_max, "con", max_edad, "años.") 
    print("El jugador con menor edad en el juego", juego, "es", nombre_min, "con", min_edad, "años.")

    linea = arch.readline().strip()
    if "--" in linea:
        print(linea)
        linea = arch.readline().strip()
        
print("Vimos", contOLD, "juegos retro")
print(contS, "juegos soccer")
print(contFPS, "juegos first person shooter")
print(contBR, "juegos battle royale")
print("Y", contR, "juegos racing")
print(f"Cometimos {errores} errores de tipeo, sowwy -w-")
print("¡Felicitaciones a todos nuestros ganadores y los veremos el siguiente año!")
