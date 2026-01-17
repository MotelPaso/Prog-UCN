
"""
Created on Sat Mar 29 16:10:19 2025
"""
continuar = "si"
total = 0
iva_total = 0
pedidos = 0
ventaMayor = 0

precio_cuarto = 5990
iva_cuarto = round(precio_cuarto - (precio_cuarto / 1.19), 3)
precio_mc = 4990
iva_mc = iva2 = round(precio_mc - (precio_mc / 1.19), 3)
precio_big = 6990
iva_big = iva3 = round(precio_big - (precio_big / 1.19), 3)

while continuar == "si":
    lleva_cuarto = False
    cant_cuarto = 0

    lleva_mc = False
    cant_mc = 0

    lleva_big = False
    cant_big = 0

    pagar = False
    print("Bienvenido a McDonald")
    print("Tenemos disponible Cuarto de libra, Mcnifica, y Big Mac")
    elegir = input("Para finalizar ponga FIN.\nQue desea ordenar? ").lower

    while elegir != "cuarto de libra" or elegir != "mcnifica" or  elegir != "big mac":  # Guardar errores
        print("Opcion erronea!, ponla otra vez.")
        elegir = input(" ")

    while elegir != "no":  # Ciclo de la eleccion.
        if elegir == "cuarto de libra":
            cant_cuarto = int(input(f"Cuesta ${precio_cuarto}, cuantas llevará?")) + cant_cuarto
            lleva_cuarto = True
            elegir = input("Quieres otra hamburguesa?")

        elif elegir == "mcnifica":
            cant_mc = int(input(f"Cuesta ${precio_mc}, cuantas llevará?")) + cant_mc
            lleva_mc = True
            elegir = input("Quieres otra hamburguesa?")

        elif elegir == "big mac":
            cant_big = int(input(f"Cuesta ${precio_big}, cuantas llevará?")) + cant_mc
            lleva_big = True
            elegir = input("Quieres otra hamburguesa?")

        elif elegir == "si":
            print("Elige una hamburguesa:")
            print("1) Cuarto de libra")
            print("2) Mcnifica")
            print("3) big mac")
            elegir = input(" ")
        elif elegir == "fin":
            pedidos -= 1
            break
        else:
            print("ocurrio un error.")
            elegir = input("quieres otra hamburguesa? ")

    if lleva_cuarto:  # Para no mostrar más de lo que compraron.
        print(f"Lleva {cant_cuarto} Cuarto de libra.")
        pagar = pagar + cant_cuarto * precio_cuarto
        iva += cant_cuarto * iva_cuarto
    if lleva_mc:
        print(f"Lleva {cant_mc} Mcnifica.")
        pagar = pagar + cant_mc * precio_mc
        iva += cant_mc * iva_mc
    if lleva_big:
        print(f"Lleva {cant_big} Big Mac.")
        pagar = pagar + cant_big * precio_big
        iva += cant_big * iva_big

    print(f"Total a pagar = ${pagar}")
    print(f"El IVA pagado en esta compra = ${iva}")
    total += pagar
    iva_total += iva
    pedidos += 1
    # ventamayor sera igual a pagar SI pagar es mayor a ventaMayor, si no, se mantiene igual
    ventaMayor = pagar if pagar > ventaMayor else ventaMayor
    continuar = input("Quiere hacer otro pedido?")

print(f"Venta mas alta: ${ventaMayor}")
print(f"Cantidad de pedidos = {pedidos}")
print(f"Monto total = ${total}")
print(f"IVA total = ${iva_total}")
