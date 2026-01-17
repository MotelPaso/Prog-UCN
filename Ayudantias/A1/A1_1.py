# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:23:07 2025

@author: Motel_Paso
"""

print("Menu:")
print("1) Convertir Kilometros a Millas")
print("2) Convertir Millas a Kilometros")
print("3) Salir del programa!")

menu = input("Elija su opcion: ") # Guardamos su opcion en una variable

if menu == "1":
    datos = input(f"Ha elegido KM a Mi.\nPonga sus KM: ")
    try:  # Primero va a correr esto
        # 1 Mi = 1.609 km
        millas = float(datos) * 1.609
        print(f"{datos} [km] son {millas} [mi]!")
    except:  # Si ponen algo malo, va a correr esto
        print("Tienes que ingresar un número, corre nuevamente el programa.")
elif menu == "2":
    datos = input("Ha elegido Mi a KM.\nPonga sus Mi: ")
    try:
        km = float(datos) / 1.609  # Convertimos a KM
        print(f"{datos} [mi] son {round(km, 3)} [km]!")
    except:
        print("Tienes que ingresar un número, corre nuevamente el programa")
elif menu == "3":
    print("Hasta luego!")
else:
    print("Eleccion no encontrada, cerrando el programa")