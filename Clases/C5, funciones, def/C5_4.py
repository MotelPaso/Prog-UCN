
"""
Created on Sat Apr 12 19:13:00 2025
"""
rep = ""
def ANILLOS(a):
    
    anillos = 0
    for i in range(len(a)):
        if "0" in a[i]:
            anillos += 1
        if "6" in a[i]:
            anillos += 1
        if "9" in a[i]:
            anillos += 1
        if "8" in a[i]:
            anillos += 2
        else:
            anillos += 0
    
    return anillos

print("Vamos a contar cuantos anillos tiene el numero")
while rep != "no":
    numero = input("Ingrese su numero, para terminar ingrese no: ")
    print("Los anillos presentes en el numero son: ", ANILLOS(numero))
    rep = input("¿Desea evaluar otro numero?") 
    
print("Adios!")