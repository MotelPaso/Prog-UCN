# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 23:04:53 2025
@author: Motel_Paso
"""
salir = ""
contador = 0
while salir != "salir":
    contador += 1
    print("Elija su asignatura!")
    print("1) Programacion")
    print("2) Programacion Avanzada")

    asig = input(":  ")
    print("Que quieres hacer?")
    print("1) Promedio Final")
    print("2) Asistencia")
    elec = input(":  ")

    if elec == "1":
        numNotas = 3
        suma = 0
        for i in range(numNotas): 
            nota = float(input("Ingrese su nota aqui: "))
            while nota > 7 or nota < 1:
                nota = float(input("nota invalida, ingrese otra: "))
            suma += nota
        promedio = suma / numNotas
        print(f"Tu promedio es {promedio}")

    elif elec == "2":
        asistidas = int(input("A cuantas clases fuiste? "))
        faltadas = int(input("A cuantas faltaste? "))
        asistenciaPromedio = asistidas * 100 / (asistidas + faltadas)
        print(f"Tu promedio de asistencia es {asistenciaPromedio}")
    salir = input('Quieres seguir viendo alumnos? Escribe [salir] para terminar: ')
print(f"Revisaste a {contador} alumnos")
print("Hasta luego")

