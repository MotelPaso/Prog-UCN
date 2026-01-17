
"""
Created on Sat Apr 12 18:35:55 2025
"""

def ventas(entrada,cantidad):
    
    if entrada == 1:
        precio = 20000 * cantidad
    if entrada == 2:
        precio = 30000 * cantidad
    if entrada == 3:
        precio = 40000 * cantidad
        
    return precio
    

print("Bienvenido a TicketMusica")
print("Tenemos 3 entradas para el evento")
print("1) Cancha -> $20.000")
print("2) Platea -> $30.000")
print("3) VIP    -> $40.000")

no = ""
ventaFinal = 0

while no != "no":

    eleccion = input("Elija su entrada:")
    posiblesElecciones = '1','2','3'
    while eleccion not in posiblesElecciones:
        print("Esa no es una opcion.")
        eleccion = int(input("Elija su entrada:"))

    cant = int(input("Cuantas quieres?"))
    while cant <= 0:
        print("No puede ser igual o menor a 0.")
        cant = int(input("Cuantas quieres?"))

    print("tu precio es: ", ventas(eleccion,cant))
    ventaFinal += ventas(eleccion,cant)

    no = input("Quieres otra entrada?").lower()

print("Tu precio final es:", ventaFinal)
