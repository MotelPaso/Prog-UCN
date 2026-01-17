"""
Created on Wed Apr  9 11:40:26 2025
"""

num_magos = 0
poder_max = 0
hechizo = 0
alqui = 0
druida = 0
ilusion = 0
elemento = 0
muerte = 0
arch = open('aprendices.txt', 'r', encoding='utf-8')

linea = arch.readline().strip()

if "Nombre" in linea:
    linea = arch.readline().strip()
    
while linea != "":
    partes = linea.split(',')
    nombre = partes[0]
    edad = int(partes[1])
    a = partes[2]
    poder_magico = int(partes[3])
    
    if a == "Hechiceria":
        hechizo += 1
    elif a == "Alquimia":
        alqui += 1
    elif a == "Druidismo":
        druida += 1
    elif a == 'Ilusionismo':
        ilusion += 1
    elif a == 'Elementalismo':
        elemento += 1
    elif a == 'Necromancia':
        muerte += 1
        
    if nombre != "":
        num_magos += 1
        
    if poder_magico > poder_max:
        poder_max = poder_magico
        nombre_max = nombre
        
    linea = arch.readline().strip()

print("Cantidad de magos:", num_magos)
print("Mayor poder magico:", poder_max, "de", nombre_max)
print("Distribucion por especialidad:")
print("Hechiceria:", hechizo)
print("Alquimia:", alqui)
print("Druidismo:", druida)
print("Ilusionismo:", ilusion)
print("Elementalismo:", elemento)
print("Necromancia:", muerte)