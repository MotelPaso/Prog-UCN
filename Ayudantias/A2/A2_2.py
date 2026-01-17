"""
Created on Sat Mar 29 14:33:51 2025
"""
cant_aprobados = 0
cant_reprobados = 0
continuar = "si"
print("calculo de aprobacion, verano 2025")

while continuar == "si":
    nota = 0
    promedio = 0
    numero_notas = 0
    while nota != -1 and numero_notas < 3:
        nota = float(input(f"Ingrese la nota {numero_notas+1}: "))
        numero_notas = numero_notas + 1

        if nota == -1:
            print("Calculando notas...")
        elif nota < 1.0 or nota > 7.0:
            print("No puede ser menor a 1.0 ni mayor a 7.0.")
            numero_notas = numero_notas - 1
        else:
            if numero_notas == 3:
                promedio += nota * 0.34
            else:
                promedio += nota * 0.33

    promedio = round(promedio, 2)
    if numero_notas > 3:
        break
    if promedio >= 4.0:
        print(f"Aprobaste, Tu promedio es {promedio}")
        cant_aprobados += 1
    else:
        print(f"Reprobaste, tu promedio es {promedio}")
        cant_reprobados += 1
    continuar = input("Quieres hacer otro?")

print(f"Alumnos aprobados = {cant_aprobados}")
print(f"Alumnos reprobados = {cant_reprobados}")
