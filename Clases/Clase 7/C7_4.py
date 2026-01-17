
"""
Created on Mon Apr 28 17:26:48 2025
"""

def esPrimo(valor):
    primo = 0
    for a in range(1,valor):
        if valor % a == 0:
            primo +=1
    if primo == 1:
        return True
    else:
        return False

def iesimoPrimo(i):
    for j in range(0,i):
        a = esPrimo(j)
        if a == True:
            b = j
    
    print(f'el iesimoPrimo es {b}')
    
numero = int(input('ingrese su numero:'))
esPrimo(numero)
i = int(input('Ingrese otro numero'))
iesimoPrimo(i)


