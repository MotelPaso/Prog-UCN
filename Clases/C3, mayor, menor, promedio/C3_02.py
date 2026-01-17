# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:32:58 2025

@author: Motel_Paso
"""

ini = int(input("Pon tu numero inicial! "))
fin = int(input("Pon tu 2do numero! "))

a = ini  # Ponemos otra variable para no cambiar el numero inicial.

for i in range(ini, fin):
    a = a + i
    print(a)
    
inter = int(input("Pon un intervalo entre los numeros! "))

for i in range(ini, fin, inter):
    print(i)