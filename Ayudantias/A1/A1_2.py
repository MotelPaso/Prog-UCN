# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 16:23:55 2025
@author Motel_Paso
"""

print('Bienvenido a Tienda Snow – ¡El invierno se acerca, equípate bien!')
print("1) Ver elegibilidad para descuento.")
print("2) Salir.")

menu = input("Elija su opcion! ")

if menu == "1":
    monto = int(input("Vamos a buscar su descuento, ingrese su monto: "))
    # Preguntamos por el monto
    if monto <= 20000:
        print(f"Su monto es {monto}")

    elif monto >= 20001 and monto <= 50000:
        print("tiene un 5% de descuento!")
        nuevo_monto = monto * 0.95 # Guardamos el nuevo monto
        print(f"Su nuevo monto es {nuevo_monto}")

    elif monto >= 50001 and monto <= 100000:
        print("Tiene un 10% de descuento!")
        nuevo_monto = monto * 0.90
        print(f"Su nuevo monto es {nuevo_monto}")

    elif monto >= 100001:
        print("Tiene un 15% de descuento!")
        nuevo_monto = monto * 0.85
        print(f"Su nuevo monto es {nuevo_monto}")
    # Revisamos valores
    if monto % 2 == 0:  # Si lo dividimos en dos y no sobra nada, es par.
        print("¡Felicidades! Jon Snow ha decidido recompensarte con un descuento extra.")
        monto2 = nuevo_monto * 0.97  # Guardamos el nuevo monto
        print(f"Su nuevo monto es {monto2}")
    if monto == nuevo_monto:
        # Si los montos son iguales, entonces no se ha hecho ningun descuento.
        print("El Guardián del Norte no ha aprobado un descuento para esta compra.")
    print("Gracias por tu compra en Tienda Snow. ¡Vuelve pronto!")

if menu == "2":
    print("Muchas gracias por visitar Tienda Snow - Que los Antiguos Dioses te acompañen.")
