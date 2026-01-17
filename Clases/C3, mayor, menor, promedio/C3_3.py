# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:57:51 2025

@author: Motel_Paso
"""

import time  # Hace que python cuente segundos

num = int(input("Un contador, pon tu numero de segundos!"))
num = num + 1  # Para hacer que empieze desde el num

for i in range(num):
    num = num - 1
    if num > 0:
        print(f"Te quedan {num} segundos")
        time.sleep(1)
    else:
        print("Termino el tiempo!")
        