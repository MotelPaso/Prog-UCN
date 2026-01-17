
"""
Created on Sat Apr 12 19:05:54 2025
"""

def esPrimo(a):
    x = a
    hola = 0
    for i in range(1,a):
        
        if x%i == 0:
            hola += 1
            
            if hola == 1:
                b = True
                
            else:
                b = False
    return b

print("Comprobar si es primo")
numero = int(input("Ingrese su numero: "))
while numero <= 1:
    print("No puede ser menor a 1")
    numero = int(input("Ingrese su numero: "))

print(esPrimo(numero))

for i in range(3,101):
    if esPrimo(i) is True:
        print(i)