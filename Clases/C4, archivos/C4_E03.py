
"""
Created on Tue Apr  1 01:49:36 2025
"""
nombre = []
edad = []
contador = 0
arch = open('ejercicio0_3.txt', "r", encoding="utf-8")
linea = arch.readline().strip()

if linea == '5':
    linea = arch.readline().strip()
'''   
while linea != "":
    if len(linea) > 3:
        nombre.append(linea)
        print(nombre)
        linea = arch.readline().strip()
    else:
        edad.append(linea)
        print(edad)
        linea = arch.readline().strip()
        
for i in range(5):
    print(nombre[i], edad[i])
'''

while linea != '':
    contador += 1
    if contador > 5:
        print(linea)
    linea = arch.readline().strip()    
    