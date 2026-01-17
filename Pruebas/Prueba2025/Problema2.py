"""
Ejercicio 2
Paulo César Araya Rojo
"""
nombre = ""
codigo = ""
contCANCHA = 0
contPLATEA = 0
contTRIBUNA = 0
contASIS = 0
contCODIGO = 0
upgrade1 = ""
contadorplatea = 0
contadortribuna = 0

print("Bienvenido al sistema del Teatro Milenario")
print("Registro de asistentes abierto...")
print("")

nombre = input("Nombre del asistente (o 'INICIARSHOW' para comenzar): ")

while nombre != "INICIARSHOW":
    sector = input("Sector original (CANCHA / PLATEA / TRIBUNA): ")
    codigo = input("¿Tiene código? (escriba 'WINTERHEART' si aplica, o presione ENTER): ")
    print("")
    
    if codigo == "WINTERHEART":
        contCODIGO += 1
        if sector == "TRIBUNA":
            sector = "PLATEA"
            contadortribuna += 1
            
        if sector == "PLATEA":
            sector = "CANCHA"
            contadorplatea += 1
    
    if contadorplatea == 1:
        upgrade1 = True
        nombre_platea = nombre
    if contadortribuna == 1:
        upgrade2 = True
        nombre_tribuna = nombre
    
    if contCANCHA <= 50:
        if sector == "CANCHA":
            contCANCHA += 1
    if contPLATEA <= 100:
        if sector == "PLATEA":
            contPLATEA += 1
    if contTRIBUNA <= 150:
        if sector == "TRIBUNA":
            contTRIBUNA += 1
            
    contASIS +=1
    nombre = input("Nombre del asistente (o 'INICIARSHOW' para comenzar): ")
    
perCANCHA = int(contCANCHA *100/contASIS)
perPLATEA = int(contPLATEA *100/contASIS)
perTRIBUNA = int(contTRIBUNA *100/contASIS)

print("ESTADÍSTICAS FINALES")
print(f"Total de asistentes registrados: {contASIS}")
print(f"Asistentes en CANCHA: {contCANCHA} ({perCANCHA}%)")
print(f"Asistentes en PLATEA: {contPLATEA} ({perPLATEA}%)")
print(f"Asistentes en TRIBUNA: {contTRIBUNA} ({perTRIBUNA}%)")
print(f"Código WINTERHEART usado: {contCODIGO} veces")
if upgrade1 == True:
    print(f"Mejor upgrade realizado por: {nombre_platea}")
if upgrade2 == True and upgrade1 != True:
    print(f"Mejor upgrade realizado por: {nombre_tribuna}")
    
