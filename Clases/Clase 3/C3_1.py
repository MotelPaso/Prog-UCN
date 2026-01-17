# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:38:41 2025

@author: Motel_Paso
"""
a = 0
num = int(input("Ingrese su numero! "))

for i in range(1, num):
    if num % i == 0: 
        a = i  # El ultimo multiplo se va a guardar
        print(a)

if a == 1: # Si es uno, es primo
    print("Es primo!")
else:
    print("No es primo!")