# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 22:36:29 2025
@author: Motel_Paso
"""
# esta es la version que hice cuando recien empeze:

for i in range(1,101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        print(i)

# Esta es la version mejorada, le suma todo a un string para compactarlo.
"""
for i in range(1,101):
    salida = ''
    if i % 3 == 0: salida += 'Fizz'
    if i % 5 == 0: salida += 'Buzz'
    if salida == '': salida += str(i)
    print(salida)
"""