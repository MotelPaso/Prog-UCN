
"""
Created on Tue Apr  1 01:49:36 2025
"""

arch = open('ejercicio0_2.txt', "r", encoding="utf-8")
linea = arch.readline().strip()

while linea != "fin":
    print(linea)
    linea = arch.readline().strip()

    