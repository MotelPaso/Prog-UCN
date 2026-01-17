"""
Paulo Araya prueba formativa 202510
"""

def reunir_datos(arch):
    linea = arch.readline().strip() # LEER LINEA
    patentes = []
    patentesUnicas = []
    porticos = []
    horas = []
    minutos = []
    while linea != '':
        partes = linea.split(';') # SPLIT
        patentes.append(partes[0])
        # partes[0] == patente
        if partes[0] not in patentesUnicas: # ordenar unicos
            patentesUnicas.append(partes[0])

        porticos.append(partes[1])

        dividirHoras = partes[2].split(':') # separar en dos listas
        horas.append(dividirHoras[0])
        minutos.append(dividirHoras[1])

        linea = arch.readline().strip()
    return patentes, porticos, horas, minutos, patentesUnicas

def reunir_pagos(arch):
    linea = arch.readline().strip()
    patentes = []
    marco = [] 
    while linea != '':
        partes = linea.split(',')
        patentes.append(partes[0].upper())
        marco.append(partes[1])
        linea = arch.readline().strip()
    return patentes, marco

def revisarViajes(salida,linea,linea2):
    horaSalida = int(horas[linea])
    minSalida = int(minutos[linea])
    tiempoSalida = (horaSalida * 60) + minSalida # 19:52 = 1192 MINUTOS
    horaLlegada = int(horas[linea2])
    minLlegada = int(minutos[linea2])
    tiempoLlegada = (horaLlegada * 60) + minLlegada # 22:02 = 1322 MINUTOS

    minTotal = tiempoLlegada - tiempoSalida # 1322 - 1192 = 130

    vPat = (dist[salida-1] * 60)/ minTotal  # en KM/h
    multa = poner_multas(vPat, vMax[salida-1])
    return multa, vPat

def poner_multas(total,maximo):
    if total > maximo+10 and total<= maximo+20:
        return 1.5
    elif total > maximo+20:
        return 3

def descontar_multas(multa, descuento):
    if descuento == 'ANTES':
        multa *= 0.50
    elif descuento == 'EXHORTO':
        multa *= 1.20
    return multa

def imprimir_infracciones(lista):
    print('1) Infracciones')
    # pasa que lo hice en base a patentes
    # y no en base a ciudades para imprimirlos
    # asi que para no ordenarlos hice esta cosa rara
    for j in range(len(ciudades)-1): # PENDEJO SE PONE VERGA
        for i in range(len(lista)):
            if f', {ciudades[j]}' in lista[i]: # revisamos por ciudad la lista
                print(lista[i])

def imprimir_total_infractor(lista):
    print('2) Total por infractor')
    for i in lista:
        print(i)

def imprimir_recaudacion(pagada,total):
    print('3) Recaudación')
    perPago = pagada *100 / total
    print(f'${round(pagada)} recaudado de ${round(total)} ({round(perPago,2)}%)')

def imprimir_morosos(morosos):
    print('4) Infractores morosos')
    print(morosos)

arch = open('radares.txt', 'r', encoding='utf-8')
pat, porticos, horas, minutos, patUnicas = reunir_datos(arch)

arch = open('pagos.txt', 'r', encoding='utf-8')
patentesPagadas, forma_pago = reunir_pagos(arch)

ciudades = ['Tongoy', 'Los Vilos', 'El Melón', 'Lamba'] 
vMax = [120, 110, 100]
dist = [206, 97, 102]

impresion1 = []
impresion2 = []
multaTotal = 0
multaPagada = 0
morosos = []

for i in range(len(patUnicas)):
    pat_Revisar = patUnicas[i] # patente a revisar
    lin_Revisar = [] # indices de las lineas a revisar
    multaLocal = 0 # multa de la patente

    for indice in range(len(pat)):
        if pat[indice] == pat_Revisar: # match
            lin_Revisar.append(indice) # guardamos los indices de las lineas a revisar

    for linea in range(len(lin_Revisar)-1):
        multa = ''
        inicio = int(porticos[lin_Revisar[linea]]) # de donde sale
        multa, vPat = revisarViajes(inicio,lin_Revisar[linea], lin_Revisar[linea+1])
        if multa: # si no es 0
            imprimir1 = (f'{pat_Revisar}, {ciudades[linea]} - {ciudades[linea+1]} {round(vPat)} km/h {multa} UTM') 
            multaLocal += multa
            impresion1.append(imprimir1) # para imprimirlo despues

    if multaLocal: # si no es 0
        if pat_Revisar in patentesPagadas: # si ya pago
            indice = patentesPagadas.index(pat_Revisar)
            multaPagada += descontar_multas(multaLocal, forma_pago[indice]) # ver descuento
        else:
            morosos.append(pat_Revisar) # no ha pagado
        imprimir = f'{pat_Revisar} {multaLocal} UTM'
        impresion2.append(imprimir) # para imprimirlo despues
    multaTotal += multaLocal

imprimir_infracciones(impresion1)
imprimir_total_infractor(impresion2)
imprimir_recaudacion(multaPagada * 52000, multaTotal*52000) # utm a dinero real
imprimir_morosos(morosos)