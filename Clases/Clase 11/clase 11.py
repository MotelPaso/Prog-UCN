"""
Yo no hice este codigo, lo dio el profe
"""

import numpy as np

def buscar_agregar(e, li):
    if e not in li:
        li.append(e)
    return li.index(e)

archivo = open('chat.txt', encoding='utf-8')
linea = archivo.readline().strip()
mensajes = np.zeros([8,12])
contador_mensajes = 0
contador_mm = 0
mensajes_multimedia = ['<Sticker>', '<GIF>', '<Imagen>', '<Audio>', '<Video>']
personas = []
while linea != '':
    contador_mensajes += 1
    partes = linea.split(';')
    fecha = partes[0].split('/')
    hora = partes[1].split(':')
    persona = partes[2]
    mensaje = partes[3]
    fila = buscar_agregar(persona, personas)
    columna = int(fecha[1]) - 1
    mensajes[fila][columna] += 1
    if mensaje in mensajes_multimedia:
        contador_mm += 1
    linea = archivo.readline().strip()
    
print(f'La cantidad de mensajes enviados es {contador_mensajes}')
porcentaje = round(contador_mm/contador_mensajes*100,2)
print(f'El porcentaje de contenido multimedia es de {porcentaje}%')
maximo = -1
indice_maximos = []
for i in range(len(personas)):
    suma = 0
    for j in range(12):
        suma += mensajes[i][j]
    print(suma)
    if suma > maximo:
        indice_maximos.clear()
        maximo = suma
        indice_maximos.append(i)
    elif suma == maximo:
        indice_maximos.append(i)
print(f'La(s) persona(s) con más mensajes enviados, con {maximo} es/son:')
for i in indice_maximos:
    print(f'- {personas[i]}')
    max_ = -1
    max_index = -1
    for j in range(12):
        if mensajes[i][j] > max_:
            max_ = mensajes[i][j]
            max_index = j
    print(f'Su mes con más mensajes fue {max_index + 1} con {mensajes[i][max_index]}')

suma_por_mes = []

for j in range(12):
    suma = 0
    for i in range(len(personas)):
        suma += mensajes[i][j]
    suma_por_mes.append(suma)

maximo_por_mes = max(suma_por_mes)
print(f'El promedio mensual de mensajes es {contador_mensajes/12} y el(los) mes(es) con más mensajes fue(ron):')
for i in range(len(suma_por_mes)):
    if suma_por_mes[i] == maximo_por_mes:
        print(f'- {i+1}')


















