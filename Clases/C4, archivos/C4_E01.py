
"""
Created on Tue Apr  1 01:30:48 2025
"""

a = 0
arch = open('ejercicio0_1.txt', "r", encoding= "utf-8")
limite = arch.readline().strip()  # Esto imprime la siguiente linea
print(limite)
linea = arch.readline().strip()

while linea != "":
    print(linea)
    linea = arch.readline().strip()
    a += 1
    if a == int(limite): # Si son 6 lineas, se corta.
        linea = ""
    
    