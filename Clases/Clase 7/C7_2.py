"""
Created on Mon Apr 28 17:01:31 2025
"""


def dividirPartes(b):
    a = b.split(',')
    inicio = int(a[0])
    fin = int(a[1])
    return inicio, fin

arch = open('rangos.txt', 'r', encoding='utf-8')

linea = arch.readline().strip()
suma = 0
while linea != '':
    
    inicio, fin = dividirPartes(linea)
    
    rango = fin - inicio
    
    rango -= 1
    suma += rango
    
    
    linea = arch.readline().strip()
    
print(suma)